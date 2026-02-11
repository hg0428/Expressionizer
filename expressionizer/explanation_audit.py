import argparse
import json
import multiprocessing as mp
import random
import signal
import time
import traceback
from typing import Any

from .equation_generation import generate_random_equation_problem
from .evaluator import EvaluatorOptions, WordingOptions, compact_evaluator_options, evaluate
from .localization import (
    build_explanation_profile,
    load_message_overrides,
    supported_profile_presets,
)
from .procedural import FUNCTIONS, ExpressionContext, generate_random_expression, seed_generation
from .render import render_latex
from .solve_equation import EquationWordingOptions, solve_equation, solve_system
from .validation import (
    compare_with_sympy,
    validate_equation_solution,
    validate_reasoning_steps,
    validate_system_solution,
)


def _mp_context():
    try:
        return mp.get_context("fork")
    except ValueError:
        return mp.get_context("spawn")


def _compare_with_sympy_timeout(
    expr: Any,
    answer: Any,
    substitutions: dict[str, Any],
    timeout_seconds: float = 2.0,
) -> dict[str, Any]:
    if timeout_seconds <= 0:
        return compare_with_sympy(expr, answer, substitutions=substitutions)
    if not hasattr(signal, "SIGALRM"):
        return compare_with_sympy(expr, answer, substitutions=substitutions)

    def _timeout_handler(_signum, _frame):
        raise TimeoutError("SymPy comparison timed out.")

    previous_handler = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.setitimer(signal.ITIMER_REAL, timeout_seconds)
    try:
        return compare_with_sympy(expr, answer, substitutions=substitutions)
    except TimeoutError:
        return {"status": "inconclusive", "reason": "sympy_timeout"}
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        signal.signal(signal.SIGALRM, previous_handler)


def _preview_substitutions(substitutions: dict[str, Any]) -> dict[str, str]:
    preview: dict[str, str] = {}
    for key, value in substitutions.items():
        if isinstance(key, str):
            try:
                preview[key] = render_latex(value)
            except Exception:
                preview[key] = str(value)
    return preview


def _render_solution(values: dict[str, Any]) -> str:
    if not values:
        return "{}"
    parts = []
    for key in sorted(values):
        try:
            rendered = render_latex(values[key])
        except Exception:
            rendered = str(values[key])
        parts.append(f"{key}={rendered}")
    return "{ " + ", ".join(parts) + " }"


def _build_eval_options(payload: dict[str, Any]) -> EvaluatorOptions:
    wording_style = payload.get("wording_style", "verbose")
    step_heading_template = payload.get("step_heading_template", "## {number}")
    explanation_profile = build_explanation_profile(
        payload.get("profile_preset"),
        locale=payload.get("locale", "en"),
        style_type=payload.get("style_type", "default"),
        message_overrides=payload.get("message_overrides", {}),
        exact_text_overrides=payload.get("exact_text_overrides", {}),
        collect_diagnostics=payload.get("collect_localization_diagnostics", False),
    )
    if payload.get("compact_explanations", False):
        options = compact_evaluator_options(
            wording_style=wording_style,
            step_heading_template=step_heading_template,
        )
        options.explanation_profile = explanation_profile
        return options
    return EvaluatorOptions(
        wording_style=wording_style,
        wording_options=WordingOptions(step_heading_template=step_heading_template),
        explanation_profile=explanation_profile,
    )


def _audit_worker(payload: dict[str, Any], output_queue: Any):
    seed = payload["seed"]
    seed_generation(seed)
    complexity = payload["complexity"]
    guarantee_solvable = payload["guarantee_solvable"]

    context = ExpressionContext()
    expr = None
    substitutions = None
    started_at = time.time()
    try:
        allowed_problem_families = {
            "sum",
            "product",
            "power",
            "function",
            "derivative",
            "integral",
        }
        allowed_equation_families = {"linear", "quadratic", "rational", "system"}
        if payload.get("problem_families"):
            invalid = sorted(
                set(payload["problem_families"]) - allowed_problem_families
            )
            if invalid:
                raise ValueError(f"Invalid problem_families: {', '.join(invalid)}")
        if payload.get("equation_families"):
            invalid = sorted(
                set(payload["equation_families"]) - allowed_equation_families
            )
            if invalid:
                raise ValueError(f"Invalid equation_families: {', '.join(invalid)}")
        eval_options = _build_eval_options(payload)
        equation_wording = EquationWordingOptions(
            step_heading_template=payload.get("step_heading_template", "## {number}"),
            explanation_profile=build_explanation_profile(
                payload.get("profile_preset"),
                locale=payload.get("locale", "en"),
                style_type=payload.get("style_type", "default"),
                message_overrides=payload.get("message_overrides", {}),
                exact_text_overrides=payload.get("exact_text_overrides", {}),
                collect_diagnostics=payload.get("collect_localization_diagnostics", False),
            ),
        )
        mode = payload.get("equation_mode", "expressions")
        if mode in ("equations", "mixed") and (
            mode == "equations" or random.random() < 0.5
        ):
            expr, variables, generated_kind = generate_random_equation_problem(
                complexity=complexity,
                mode="mixed",
                equation_families=payload.get("equation_families"),
            )
            if generated_kind in ("equation", "quadratic_equation", "rational_equation"):
                solution, solve_context = solve_equation(
                    expr,
                    variable=variables[0],
                    wording_options=equation_wording,
                )
                answer = solution.values
                rendered = solve_context.render()
                reasoning_check = {
                    "valid": len(rendered.strip()) > 0 and "None" not in rendered,
                    "failure_count": 0 if "None" not in rendered else 1,
                    "failures": [] if "None" not in rendered else [{"type": "render_contains_none"}],
                    "notes": [],
                    "rendered_length": len(rendered),
                }
                sympy_check = (
                    validate_equation_solution(expr, solution.values)
                    if payload["sympy_compare"]
                    else {"status": "skipped"}
                )
            else:
                solution, solve_context = solve_system(
                    expr,
                    variables=variables,
                    wording_options=equation_wording,
                )
                answer = solution.values
                rendered = solve_context.render()
                reasoning_check = {
                    "valid": len(rendered.strip()) > 0 and "None" not in rendered,
                    "failure_count": 0 if "None" not in rendered else 1,
                    "failures": [] if "None" not in rendered else [{"type": "render_contains_none"}],
                    "notes": [],
                    "rendered_length": len(rendered),
                }
                sympy_check = (
                    validate_system_solution(expr, solution.values)
                    if payload["sympy_compare"]
                    else {"status": "skipped"}
                )
        else:
            expr = generate_random_expression(
                max_depth=payload["max_depth"],
                allow_calculus=payload["allow_calculus"],
                allow_definite_integrals=payload["allow_definite_integrals"],
                max_derivative_order=payload["max_derivative_order"],
                complexity=complexity,
                guarantee_solvable=guarantee_solvable,
                generation_profile=payload.get("generation_profile", "realistic"),
                solvability_mode=payload.get("solvability_mode", "mixed"),
                unsolvable_probability=payload.get("unsolvable_probability", 0.12),
                hard_problem_probability=payload.get("hard_problem_probability", 0.2),
                problem_families=payload.get("problem_families"),
                context=context,
            )
            substitutions = context.substitutions.copy()
            substitutions.update(FUNCTIONS)

            answer, eval_context = evaluate(
                expr,
                substitutions=substitutions,
                error_on_invalid_snap=False,
                options=eval_options,
            )
            reasoning_check = validate_reasoning_steps(eval_context, answer)
            sympy_check = (
                _compare_with_sympy_timeout(expr, answer, substitutions)
                if payload["sympy_compare"]
                else {"status": "skipped"}
            )
            if eval_context.is_approximate and sympy_check.get("status") == "conflict":
                sympy_check = {
                    **sympy_check,
                    "status": "inconclusive",
                    "reason": "approximation_enabled",
                }

        output_queue.put(
            {
                "status": "ok",
                "seed": seed,
                "index": payload["index"],
                "complexity": complexity,
                "guarantee_solvable": guarantee_solvable,
                "duration_seconds": round(time.time() - started_at, 6),
                "expression_latex": render_latex(expr),
                "answer_latex": render_latex(answer)
                if not isinstance(answer, dict)
                else _render_solution(answer),
                "reasoning_check": reasoning_check,
                "sympy_check": sympy_check,
                "substitutions": _preview_substitutions(context.substitutions),
                "intended_unsolvable_reason": getattr(
                    context, "intended_unsolvable_reason", None
                ),
                "generated_problem_family": getattr(
                    context, "generated_problem_family", None
                ),
                "localization_diagnostics": getattr(
                    eval_context, "localization_diagnostics", {}
                )
                if "eval_context" in locals()
                else (
                    solve_context.localizer.diagnostics()
                    if "solve_context" in locals()
                    and getattr(solve_context, "localizer", None) is not None
                    else {}
                ),
            }
        )
    except Exception as exc:
        output_queue.put(
            {
                "status": "error",
                "seed": seed,
                "index": payload["index"],
                "complexity": complexity,
                "guarantee_solvable": guarantee_solvable,
                "duration_seconds": round(time.time() - started_at, 6),
                "exception_type": type(exc).__name__,
                "exception_message": str(exc),
                "traceback": traceback.format_exc(),
                "expression_latex": render_latex(expr) if expr is not None else None,
                "substitutions": _preview_substitutions(context.substitutions),
            }
        )


def _run_case_with_timeout(payload: dict[str, Any], timeout_seconds: float) -> dict[str, Any]:
    def _run_once(timeout: float) -> dict[str, Any]:
        ctx = _mp_context()
        output_queue = ctx.Queue()
        process = ctx.Process(target=_audit_worker, args=(payload, output_queue))
        try:
            process.start()
            process.join(timeout)

            if process.is_alive():
                process.terminate()
                process.join(2)
                return {
                    "status": "hang",
                    "seed": payload["seed"],
                    "index": payload["index"],
                    "complexity": payload["complexity"],
                    "guarantee_solvable": payload["guarantee_solvable"],
                    "timeout_seconds": timeout,
                }

            if not output_queue.empty():
                return output_queue.get()

            return {
                "status": "error",
                "seed": payload["seed"],
                "index": payload["index"],
                "complexity": payload["complexity"],
                "guarantee_solvable": payload["guarantee_solvable"],
                "exception_type": "NoWorkerOutput",
                "exception_message": "Audit worker exited without output.",
            }
        finally:
            try:
                output_queue.close()
                output_queue.join_thread()
            except Exception:
                pass
            try:
                process.close()
            except Exception:
                pass

    result = _run_once(timeout_seconds)
    if result["status"] != "hang":
        return result

    retry = _run_once(timeout_seconds * 2)
    if retry["status"] != "hang":
        if retry["status"] == "ok":
            retry["retry_after_hang"] = True
        return retry

    final_retry = _run_once(timeout_seconds * 4)
    if final_retry["status"] == "ok":
        final_retry["retry_after_hang"] = True
    return final_retry


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate random problems and explanations, then audit step-by-step "
            + "reasoning integrity and optional SymPy equivalence."
        )
    )
    parser.add_argument("--cases", type=int, default=100)
    parser.add_argument("--base-seed", type=int, default=9001)
    parser.add_argument("--max-depth", type=int, default=4)
    parser.add_argument(
        "--complexity-cycle",
        type=lambda s: [float(p.strip()) for p in s.split(",") if p.strip()],
        default=[0.2, 0.5, 0.8],
    )
    parser.add_argument("--allow-calculus", action="store_true", default=True)
    parser.add_argument("--allow-definite-integrals", action="store_true", default=True)
    parser.add_argument("--max-derivative-order", type=int, default=2)
    parser.add_argument("--sympy-compare", action="store_true", default=False)
    parser.add_argument(
        "--generation-profile",
        choices=["realistic", "stress"],
        default="realistic",
    )
    parser.add_argument(
        "--solvability-mode",
        choices=["mixed", "solvable", "unsolvable"],
        default="mixed",
    )
    parser.add_argument("--unsolvable-probability", type=float, default=0.12)
    parser.add_argument("--hard-problem-probability", type=float, default=0.2)
    parser.add_argument(
        "--equation-mode",
        choices=["expressions", "equations", "mixed"],
        default="expressions",
    )
    parser.add_argument("--timeout-seconds", type=float, default=10.0)
    parser.add_argument("--report-every", type=int, default=20)
    parser.add_argument(
        "--wording-style",
        choices=["verbose", "concise"],
        default="verbose",
    )
    parser.add_argument(
        "--compact-explanations",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--step-heading-template",
        type=str,
        default="## {number}",
    )
    parser.add_argument("--locale", type=str, default="en")
    parser.add_argument(
        "--style-type",
        choices=["default", "compact", "plain", "xml"],
        default="default",
    )
    parser.add_argument(
        "--profile-preset",
        choices=supported_profile_presets(),
        default=None,
    )
    parser.add_argument(
        "--collect-localization-diagnostics",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--problem-families",
        type=lambda s: [p.strip() for p in s.split(",") if p.strip()],
        default=None,
    )
    parser.add_argument(
        "--equation-families",
        type=lambda s: [p.strip() for p in s.split(",") if p.strip()],
        default=None,
    )
    parser.add_argument(
        "--messages-file",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--exact-text-overrides-file",
        type=str,
        default=None,
    )
    args = parser.parse_args()
    if any(v < 0.0 or v > 1.0 for v in args.complexity_cycle):
        raise ValueError("--complexity-cycle values must be in [0, 1].")
    if not (0.0 <= args.unsolvable_probability <= 1.0):
        raise ValueError("--unsolvable-probability must be in [0, 1].")
    if not (0.0 <= args.hard_problem_probability <= 1.0):
        raise ValueError("--hard-problem-probability must be in [0, 1].")
    if args.problem_families:
        allowed = {"sum", "product", "power", "function", "derivative", "integral"}
        invalid = sorted(set(args.problem_families) - allowed)
        if invalid:
            raise ValueError(f"Invalid --problem-families values: {', '.join(invalid)}")
    if args.equation_families:
        allowed = {"linear", "quadratic", "rational", "system"}
        invalid = sorted(set(args.equation_families) - allowed)
        if invalid:
            raise ValueError(f"Invalid --equation-families values: {', '.join(invalid)}")
    message_overrides = (
        load_message_overrides(args.messages_file) if args.messages_file else {}
    )
    exact_text_overrides = (
        load_message_overrides(args.exact_text_overrides_file)
        if args.exact_text_overrides_file
        else {}
    )

    started = time.time()
    failures: list[dict[str, Any]] = []
    reasoning_failures = 0
    sympy_conflicts = 0
    sympy_inconclusive = 0
    runtime_errors = 0
    hangs = 0

    for index in range(args.cases):
        seed = args.base_seed + index
        complexity = args.complexity_cycle[index % len(args.complexity_cycle)]
        guarantee_solvable = (index % 2) == 0

        payload = {
            "index": index,
            "seed": seed,
            "complexity": complexity,
            "guarantee_solvable": guarantee_solvable,
            "max_depth": args.max_depth,
            "allow_calculus": args.allow_calculus,
            "allow_definite_integrals": args.allow_definite_integrals,
            "max_derivative_order": args.max_derivative_order,
            "sympy_compare": args.sympy_compare,
            "equation_mode": args.equation_mode,
            "generation_profile": args.generation_profile,
            "solvability_mode": args.solvability_mode,
            "unsolvable_probability": args.unsolvable_probability,
            "hard_problem_probability": args.hard_problem_probability,
            "wording_style": args.wording_style,
            "compact_explanations": args.compact_explanations,
            "step_heading_template": args.step_heading_template,
            "locale": args.locale,
            "style_type": args.style_type,
            "profile_preset": args.profile_preset,
            "collect_localization_diagnostics": args.collect_localization_diagnostics,
            "problem_families": args.problem_families,
            "equation_families": args.equation_families,
            "message_overrides": message_overrides,
            "exact_text_overrides": exact_text_overrides,
        }
        result = _run_case_with_timeout(payload, args.timeout_seconds)

        if result["status"] == "hang":
            hangs += 1
            failures.append({"type": "hang", **result})
        elif result["status"] == "error":
            runtime_errors += 1
            failures.append({"type": "runtime_error", **result})
        else:
            reasoning_check = result["reasoning_check"]
            if not reasoning_check.get("valid", False):
                reasoning_failures += 1
                failures.append({"type": "reasoning_failure", **result})

            sympy_check = result["sympy_check"]
            if sympy_check.get("status") == "conflict":
                sympy_conflicts += 1
                failures.append({"type": "sympy_conflict", **result})
            elif sympy_check.get("status") == "inconclusive":
                sympy_inconclusive += 1

        completed = index + 1
        if completed % max(1, args.report_every) == 0:
            elapsed = round(time.time() - started, 3)
            print(
                f"[audit] {completed}/{args.cases} completed, "
                + f"runtime_errors={runtime_errors}, hangs={hangs}, "
                + f"reasoning_failures={reasoning_failures}, "
                + f"sympy_conflicts={sympy_conflicts}, "
                + f"inconclusive={sympy_inconclusive}, elapsed={elapsed}s"
            )

    summary = {
        "cases": args.cases,
        "reasoning_failures": reasoning_failures,
        "sympy_conflicts": sympy_conflicts,
        "sympy_inconclusive": sympy_inconclusive,
        "runtime_errors": runtime_errors,
        "hangs": hangs,
        "total_failures": len(failures),
        "elapsed_seconds": round(time.time() - started, 3),
    }
    print("\n=== EXPLANATION AUDIT SUMMARY ===")
    print(json.dumps(summary, indent=2, sort_keys=True))

    if failures:
        print("\n=== SAMPLE FAILURES (up to 10) ===")
        print(json.dumps(failures[:10], indent=2, sort_keys=True))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
