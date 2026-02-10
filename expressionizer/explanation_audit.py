import argparse
import json
import multiprocessing as mp
import random
import time
import traceback
from typing import Any

import numpy as np

from .evaluator import evaluate
from .procedural import FUNCTIONS, ExpressionContext, generate_random_expression
from .render import render_latex
from .validation import compare_with_sympy, validate_reasoning_steps


def _mp_context():
    try:
        return mp.get_context("fork")
    except ValueError:
        return mp.get_context("spawn")


def _preview_substitutions(substitutions: dict[str, Any]) -> dict[str, str]:
    preview: dict[str, str] = {}
    for key, value in substitutions.items():
        if isinstance(key, str):
            try:
                preview[key] = render_latex(value)
            except Exception:
                preview[key] = str(value)
    return preview


def _audit_worker(payload: dict[str, Any], output_queue: Any):
    seed = payload["seed"]
    random.seed(seed)
    np.random.seed(seed)
    difficulty = payload["difficulty"]
    guarantee_solvable = payload["guarantee_solvable"]

    context = ExpressionContext()
    expr = None
    substitutions = None
    started_at = time.time()
    try:
        expr = generate_random_expression(
            max_depth=payload["max_depth"],
            allow_calculus=payload["allow_calculus"],
            allow_definite_integrals=payload["allow_definite_integrals"],
            max_derivative_order=payload["max_derivative_order"],
            difficulty=difficulty,
            guarantee_solvable=guarantee_solvable,
            context=context,
        )
        substitutions = context.substitutions.copy()
        substitutions.update(FUNCTIONS)

        answer, eval_context = evaluate(
            expr,
            substitutions=substitutions,
            error_on_invalid_snap=False,
        )
        reasoning_check = validate_reasoning_steps(eval_context, answer)
        sympy_check = (
            compare_with_sympy(expr, answer, substitutions=substitutions)
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
                "difficulty": difficulty,
                "guarantee_solvable": guarantee_solvable,
                "duration_seconds": round(time.time() - started_at, 6),
                "expression_latex": render_latex(expr),
                "answer_latex": render_latex(answer),
                "reasoning_check": reasoning_check,
                "sympy_check": sympy_check,
                "substitutions": _preview_substitutions(context.substitutions),
            }
        )
    except Exception as exc:
        output_queue.put(
            {
                "status": "error",
                "seed": seed,
                "index": payload["index"],
                "difficulty": difficulty,
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
                    "difficulty": payload["difficulty"],
                    "guarantee_solvable": payload["guarantee_solvable"],
                    "timeout_seconds": timeout,
                }

            if not output_queue.empty():
                return output_queue.get()

            return {
                "status": "error",
                "seed": payload["seed"],
                "index": payload["index"],
                "difficulty": payload["difficulty"],
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
        "--difficulty-cycle",
        type=lambda s: [p.strip() for p in s.split(",") if p.strip()],
        default=["beginner", "intermediate", "advanced"],
    )
    parser.add_argument("--allow-calculus", action="store_true", default=True)
    parser.add_argument("--allow-definite-integrals", action="store_true", default=True)
    parser.add_argument("--max-derivative-order", type=int, default=2)
    parser.add_argument("--sympy-compare", action="store_true", default=False)
    parser.add_argument("--timeout-seconds", type=float, default=10.0)
    parser.add_argument("--report-every", type=int, default=20)
    args = parser.parse_args()

    started = time.time()
    failures: list[dict[str, Any]] = []
    reasoning_failures = 0
    sympy_conflicts = 0
    sympy_inconclusive = 0

    for index in range(args.cases):
        seed = args.base_seed + index
        difficulty = args.difficulty_cycle[index % len(args.difficulty_cycle)]
        guarantee_solvable = (index % 2) == 0

        payload = {
            "index": index,
            "seed": seed,
            "difficulty": difficulty,
            "guarantee_solvable": guarantee_solvable,
            "max_depth": args.max_depth,
            "allow_calculus": args.allow_calculus,
            "allow_definite_integrals": args.allow_definite_integrals,
            "max_derivative_order": args.max_derivative_order,
            "sympy_compare": args.sympy_compare,
        }
        result = _run_case_with_timeout(payload, args.timeout_seconds)

        if result["status"] == "hang":
            failures.append({"type": "hang", **result})
        elif result["status"] == "error":
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
                + f"reasoning_failures={reasoning_failures}, "
                + f"sympy_conflicts={sympy_conflicts}, "
                + f"inconclusive={sympy_inconclusive}, elapsed={elapsed}s"
            )

    summary = {
        "cases": args.cases,
        "reasoning_failures": reasoning_failures,
        "sympy_conflicts": sympy_conflicts,
        "sympy_inconclusive": sympy_inconclusive,
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
