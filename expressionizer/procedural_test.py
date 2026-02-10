import argparse
import json
import multiprocessing as mp
import random
import time
import traceback
from dataclasses import asdict, dataclass
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


@dataclass
class CaseProfile:
    name: str
    difficulty: str
    guarantee_solvable: bool


def _build_profiles(mode: str, difficulty_cycle: list[str]) -> list[CaseProfile]:
    profiles: list[CaseProfile] = []
    for difficulty in difficulty_cycle:
        if mode in ("always", "mixed"):
            profiles.append(
                CaseProfile(
                    name=f"{difficulty}_solvable",
                    difficulty=difficulty,
                    guarantee_solvable=True,
                )
            )
        if mode in ("never", "mixed"):
            profiles.append(
                CaseProfile(
                    name=f"{difficulty}_unspecified",
                    difficulty=difficulty,
                    guarantee_solvable=False,
                )
            )
    return profiles


def _safe_render_latex(expr: Any) -> str:
    try:
        return render_latex(expr)
    except Exception:
        return "<latex-render-failed>"


def _worker(payload: dict[str, Any], output_queue: Any):
    seed = payload["seed"]
    random.seed(seed)
    np.random.seed(seed)

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
            difficulty=payload["difficulty"],
            guarantee_solvable=payload["guarantee_solvable"],
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
            if payload.get("sympy_compare", False)
            else {"status": "skipped", "reason": "disabled"}
        )
        sympy_conflict = sympy_check.get("status") == "conflict"
        reasoning_valid = bool(reasoning_check.get("valid", False))

        if eval_context.is_approximate and sympy_conflict:
            sympy_check = {
                **sympy_check,
                "status": "inconclusive",
                "reason": "approximation_enabled",
            }
            sympy_conflict = False

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
                "answer_latex": _safe_render_latex(answer),
                "solve_status": eval_context.solve_status,
                "reason_code": eval_context.reason_code,
                "coverage_tags": sorted(eval_context.coverage_tags),
                "events_count": len(eval_context.explanation_events),
                "reasoning_check": reasoning_check,
                "sympy_check": sympy_check,
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
        + f"--difficulty-cycle {','.join(args.difficulty_cycle)}"
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
        "--difficulty-cycle",
        type=lambda s: [p.strip() for p in s.split(",") if p.strip()],
        default=["beginner", "intermediate", "advanced"],
        help="Comma-separated profile cycle of difficulties.",
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
    args = parser.parse_args()

    profiles = _build_profiles(args.guarantee_solvable_mode, args.difficulty_cycle)
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
            "difficulty": profile.difficulty,
            "guarantee_solvable": profile.guarantee_solvable,
            "max_depth": args.max_depth,
            "allow_calculus": args.allow_calculus,
            "allow_definite_integrals": args.allow_definite_integrals,
            "max_derivative_order": args.max_derivative_order,
            "sympy_compare": args.sympy_compare,
            "sympy_strict": args.sympy_strict,
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
