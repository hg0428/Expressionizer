import argparse
import json
import multiprocessing as mp
import random
import signal
import time
import traceback
from dataclasses import asdict, dataclass
from typing import Any

from .evaluator import EvaluatorOptions, WordingOptions, compact_evaluator_options, evaluate
from .localization import (
    ExplanationProfile,
    build_explanation_profile,
    load_message_overrides,
    supported_profile_presets,
)
from .equation_generation import generate_random_equation_problem
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


@dataclass
class CaseProfile:
    name: str
    complexity: float
    guarantee_solvable: bool


def _build_profiles(mode: str, complexity_cycle: list[float]) -> list[CaseProfile]:
    profiles: list[CaseProfile] = []
    for complexity in complexity_cycle:
        label = f"c{complexity:.2f}"
        if mode in ("always", "mixed"):
            profiles.append(
                CaseProfile(
                    name=f"{label}_solvable",
                    complexity=complexity,
                    guarantee_solvable=True,
                )
            )
        if mode in ("never", "mixed"):
            profiles.append(
                CaseProfile(
                    name=f"{label}_unspecified",
                    complexity=complexity,
                    guarantee_solvable=False,
                )
            )
    return profiles


def _safe_render_latex(expr: Any) -> str:
    try:
        return render_latex(expr)
    except Exception:
        return "<latex-render-failed>"


def _render_solution(values: dict[str, Any]) -> str:
    if not values:
        return "{}"
    parts = []
    for key in sorted(values):
        value = values[key]
        if isinstance(value, (int, float)):
            rendered_value = str(value)
        else:
            rendered_value = _safe_render_latex(value)
        parts.append(f"{key}={rendered_value}")
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


def _worker(payload: dict[str, Any], output_queue: Any):
    seed = payload["seed"]
    seed_generation(seed)

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
                complexity=payload["complexity"],
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
                reasoning_check = {
                    "valid": len(solve_context.render().strip()) > 0
                    and "None" not in solve_context.render(),
                    "failure_count": 0 if "None" not in solve_context.render() else 1,
                    "failures": [] if "None" not in solve_context.render() else [{"type": "render_contains_none"}],
                    "notes": [],
                    "rendered_length": len(solve_context.render()),
                }
                sympy_check = (
                    validate_equation_solution(expr, solution.values)
                    if payload.get("sympy_compare", False)
                    else {"status": "skipped", "reason": "disabled"}
                )
                solve_status = solution.status
                reason_code = solution.reason_code
            else:
                solution, solve_context = solve_system(
                    expr,
                    variables=variables,
                    wording_options=equation_wording,
                )
                answer = solution.values
                reasoning_check = {
                    "valid": len(solve_context.render().strip()) > 0
                    and "None" not in solve_context.render(),
                    "failure_count": 0 if "None" not in solve_context.render() else 1,
                    "failures": [] if "None" not in solve_context.render() else [{"type": "render_contains_none"}],
                    "notes": [],
                    "rendered_length": len(solve_context.render()),
                }
                sympy_check = (
                    validate_system_solution(expr, solution.values)
                    if payload.get("sympy_compare", False)
                    else {"status": "skipped", "reason": "disabled"}
                )
                solve_status = solution.status
                reason_code = solution.reason_code
        else:
            expr = generate_random_expression(
                max_depth=payload["max_depth"],
                allow_calculus=payload["allow_calculus"],
                allow_definite_integrals=payload["allow_definite_integrals"],
                max_derivative_order=payload["max_derivative_order"],
                complexity=payload["complexity"],
                guarantee_solvable=payload["guarantee_solvable"],
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
                if payload.get("sympy_compare", False)
                else {"status": "skipped", "reason": "disabled"}
            )
            if eval_context.is_approximate and sympy_check.get("status") == "conflict":
                sympy_check = {
                    **sympy_check,
                    "status": "inconclusive",
                    "reason": "approximation_enabled",
                }
            solve_status = eval_context.solve_status
            reason_code = eval_context.reason_code

        sympy_conflict = sympy_check.get("status") == "conflict"
        reasoning_valid = bool(reasoning_check.get("valid", False))

        if sympy_conflict and payload.get("sympy_strict", False) and not reasoning_valid:
            output_queue.put(
                {
                    "status": "error",
                    "seed": seed,
                    "profile": payload["profile_name"],
                    "duration_seconds": round(time.time() - started_at, 6),
                    "exception_type": "SympyConflictAndReasoningInvalid",
                    "exception_message": "SymPy comparison disagreed and step reasoning replay failed.",
                    "expression_latex": _safe_render_latex(expr),
                    "answer_latex": _safe_render_latex(answer),
                    "sympy_check": sympy_check,
                    "reasoning_check": reasoning_check,
                }
            )
            return

        output_queue.put(
            {
                "status": "ok",
                "seed": seed,
                "profile": payload["profile_name"],
                "duration_seconds": round(time.time() - started_at, 6),
                "expression_latex": _safe_render_latex(expr),
                "answer_latex": _safe_render_latex(answer)
                if not isinstance(answer, dict)
                else _render_solution(answer),
                "solve_status": solve_status,
                "reason_code": reason_code,
                "intended_unsolvable_reason": getattr(
                    context, "intended_unsolvable_reason", None
                ),
                "generated_problem_family": getattr(
                    context, "generated_problem_family", None
                ),
                "coverage_tags": sorted(getattr(eval_context, "coverage_tags", set()))
                if "eval_context" in locals()
                else [],
                "events_count": len(getattr(eval_context, "explanation_events", []))
                if "eval_context" in locals()
                else 0,
                "reasoning_check": reasoning_check,
                "sympy_check": sympy_check,
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
                "profile": payload["profile_name"],
                "duration_seconds": round(time.time() - started_at, 6),
                "exception_type": type(exc).__name__,
                "exception_message": str(exc),
                "traceback": traceback.format_exc(),
                "expression_latex": _safe_render_latex(expr) if expr is not None else None,
                "substitutions_preview": {
                    k: _safe_render_latex(v)
                    for k, v in (substitutions or {}).items()
                    if isinstance(k, str)
                },
            }
        )


def _run_case_with_timeout(payload: dict[str, Any], timeout_seconds: float) -> dict[str, Any]:
    def _run_once(timeout: float) -> dict[str, Any]:
        ctx = _mp_context()
        output_queue = ctx.Queue()
        process = ctx.Process(target=_worker, args=(payload, output_queue))
        try:
            process.start()
            process.join(timeout)

            if process.is_alive():
                process.terminate()
                process.join(2)
                return {
                    "status": "hang",
                    "seed": payload["seed"],
                    "profile": payload["profile_name"],
                    "timeout_seconds": timeout,
                }

            if not output_queue.empty():
                return output_queue.get()

            return {
                "status": "error",
                "seed": payload["seed"],
                "profile": payload["profile_name"],
                "exception_type": "NoWorkerOutput",
                "exception_message": "Worker process exited without emitting output.",
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


def _print_failure_and_repro(result: dict[str, Any], args: argparse.Namespace):
    print("\n=== PROCEDURAL FAILURE DETECTED ===")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("\nRepro command:")
    print(
        "python -m expressionizer.procedural_test "
        + f"--base-seed {result['seed']} --max-cases 1 "
        + f"--timeout-seconds {args.timeout_seconds} "
        + f"--max-depth {args.max_depth} "
        + f"--guarantee-solvable-mode {args.guarantee_solvable_mode} "
        + f"--complexity-cycle {','.join(str(v) for v in args.complexity_cycle)} "
        + f"--equation-mode {args.equation_mode} "
        + f"--generation-profile {args.generation_profile} "
        + f"--solvability-mode {args.solvability_mode} "
        + f"--unsolvable-probability {args.unsolvable_probability} "
        + f"--hard-problem-probability {args.hard_problem_probability} "
        + f"--wording-style {args.wording_style} "
        + ("--compact-explanations " if args.compact_explanations else "")
        + f"--step-heading-template {json.dumps(args.step_heading_template)} "
        + f"--locale {args.locale} "
        + f"--style-type {args.style_type} "
        + (
            f"--profile-preset {json.dumps(args.profile_preset)} "
            if args.profile_preset
            else ""
        )
        + (
            "--collect-localization-diagnostics "
            if args.collect_localization_diagnostics
            else ""
        )
        + (
            f"--problem-families {json.dumps(','.join(args.problem_families))} "
            if args.problem_families
            else ""
        )
        + (
            f"--equation-families {json.dumps(','.join(args.equation_families))} "
            if args.equation_families
            else ""
        )
        + (f"--messages-file {json.dumps(args.messages_file)} " if args.messages_file else "")
        + (
            f"--exact-text-overrides-file {json.dumps(args.exact_text_overrides_file)}"
            if args.exact_text_overrides_file
            else ""
        )
    )


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Procedural stress test: keep generating problems and solutions until "
            + "a hang or error is found."
        )
    )
    parser.add_argument(
        "--base-seed",
        type=int,
        default=1337,
        help="Seed used for deterministic reproduction (case i uses base_seed + i).",
    )
    parser.add_argument(
        "--max-cases",
        type=int,
        default=0,
        help="Stop after N cases (0 means run indefinitely until failure).",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=10.0,
        help="Per-case timeout; case is treated as hang after this limit.",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=4,
        help="Generation max depth passed to procedural generator.",
    )
    parser.add_argument(
        "--allow-calculus",
        action="store_true",
        default=True,
        help="Enable calculus generation.",
    )
    parser.add_argument(
        "--allow-definite-integrals",
        action="store_true",
        default=True,
        help="Enable definite integral generation.",
    )
    parser.add_argument(
        "--max-derivative-order",
        type=int,
        default=2,
        help="Max derivative order for generated calculus expressions.",
    )
    parser.add_argument(
        "--guarantee-solvable-mode",
        choices=["always", "never", "mixed"],
        default="mixed",
        help="How to set guarantee_solvable across test profiles.",
    )
    parser.add_argument(
        "--complexity-cycle",
        type=lambda s: [float(p.strip()) for p in s.split(",") if p.strip()],
        default=[0.2, 0.5, 0.8],
        help="Comma-separated profile cycle of complexity values in [0, 1].",
    )
    parser.add_argument(
        "--report-every",
        type=int,
        default=25,
        help="Print progress every N successful cases.",
    )
    parser.add_argument(
        "--sympy-compare",
        action="store_true",
        default=False,
        help="Cross-check each case against SymPy for equivalence.",
    )
    parser.add_argument(
        "--sympy-strict",
        action="store_true",
        default=False,
        help=(
            "Fail on SymPy conflicts only when reasoning replay also fails "
            + "(requires --sympy-compare)."
        ),
    )
    parser.add_argument(
        "--equation-mode",
        choices=["expressions", "equations", "mixed"],
        default="expressions",
        help="Generate classic expressions, equation problems, or a mix.",
    )
    parser.add_argument(
        "--generation-profile",
        choices=["realistic", "stress"],
        default="realistic",
        help="Expression generation profile: realistic (shorter/user-facing) or stress (broader/extreme).",
    )
    parser.add_argument(
        "--solvability-mode",
        choices=["mixed", "solvable", "unsolvable"],
        default="mixed",
        help="Control how often generated expression problems are intentionally unsolvable.",
    )
    parser.add_argument(
        "--unsolvable-probability",
        type=float,
        default=0.12,
        help="When solvability-mode=mixed, probability of injecting intentionally unsolvable expression cases.",
    )
    parser.add_argument(
        "--hard-problem-probability",
        type=float,
        default=0.2,
        help="Probability of promoting a realistic case to a harder variant.",
    )
    parser.add_argument(
        "--wording-style",
        choices=["verbose", "concise"],
        default="verbose",
        help="Choose explanation wording style for expression evaluation.",
    )
    parser.add_argument(
        "--compact-explanations",
        action="store_true",
        default=False,
        help="Use compact explanation preset (fewer decomposition/table details).",
    )
    parser.add_argument(
        "--step-heading-template",
        type=str,
        default="## {number}",
        help="Template for section headings, e.g. '### Phase {number}'.",
    )
    parser.add_argument("--locale", type=str, default="en")
    parser.add_argument(
        "--style-type",
        choices=["default", "compact", "plain", "xml"],
        default="default",
        help="Built-in rendering style overlay.",
    )
    parser.add_argument(
        "--profile-preset",
        choices=supported_profile_presets(),
        default=None,
        help="Optional preset bundle for locale/style defaults.",
    )
    parser.add_argument(
        "--collect-localization-diagnostics",
        action="store_true",
        default=False,
        help="Collect key usage/fallback diagnostics while rendering explanations.",
    )
    parser.add_argument(
        "--problem-families",
        type=lambda s: [p.strip() for p in s.split(",") if p.strip()],
        default=None,
        help="Comma-separated expression families: sum,product,power,function,derivative,integral",
    )
    parser.add_argument(
        "--equation-families",
        type=lambda s: [p.strip() for p in s.split(",") if p.strip()],
        default=None,
        help="Comma-separated equation families: linear,quadratic,rational,system",
    )
    parser.add_argument(
        "--messages-file",
        type=str,
        default=None,
        help="Optional JSON map for key-based template overrides.",
    )
    parser.add_argument(
        "--exact-text-overrides-file",
        type=str,
        default=None,
        help="Optional JSON map for exact text replacement overrides.",
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

    profiles = _build_profiles(args.guarantee_solvable_mode, args.complexity_cycle)
    if len(profiles) == 0:
        raise ValueError("No profiles configured.")

    started = time.time()
    case_count = 0
    while True:
        if args.max_cases > 0 and case_count >= args.max_cases:
            elapsed = round(time.time() - started, 3)
            print(
                f"Completed {case_count} cases without hangs/errors in {elapsed}s."
            )
            return 0

        seed = args.base_seed + case_count
        profile = profiles[case_count % len(profiles)]
        payload = {
            "seed": seed,
            "profile_name": profile.name,
            "complexity": profile.complexity,
            "guarantee_solvable": profile.guarantee_solvable,
            "max_depth": args.max_depth,
            "allow_calculus": args.allow_calculus,
            "allow_definite_integrals": args.allow_definite_integrals,
            "max_derivative_order": args.max_derivative_order,
            "sympy_compare": args.sympy_compare,
            "sympy_strict": args.sympy_strict,
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
        if result["status"] in ("error", "hang"):
            _print_failure_and_repro(result, args)
            return 1

        case_count += 1
        if case_count % max(1, args.report_every) == 0:
            elapsed = round(time.time() - started, 3)
            print(
                f"[ok] {case_count} cases, last seed={seed}, profile={profile.name}, elapsed={elapsed}s"
            )


if __name__ == "__main__":
    raise SystemExit(main())
