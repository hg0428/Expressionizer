import argparse
import math
import random
from pathlib import Path

import numpy as np

from .evaluator import CalculatorModeOptions, EvaluatorOptions, evaluate
from .procedural import FUNCTIONS, ExpressionContext, generate_random_expression
from .render import render_latex


def _review_render(value):
    if isinstance(value, (int, float)):
        abs_value = abs(value)
        if abs_value != 0 and (abs_value >= 1e8 or abs_value < 1e-8):
            coefficient, exponent = f"{value:.8e}".split("e")
            coefficient = coefficient.rstrip("0").rstrip(".")
            exponent_value = int(exponent)
            return f"{coefficient} \\times 10^{{{exponent_value}}}"
        if isinstance(value, float) and math.isfinite(value):
            return str(float(f"{value:.15g}"))
    return render_latex(value)


def _build_case(
    case_index: int,
    base_seed: int,
    max_depth: int,
    generation_profile: str,
    calculator_mode_enabled: bool,
):
    seed = base_seed + case_index
    difficulty_cycle = ["beginner", "intermediate", "advanced"]
    difficulty = difficulty_cycle[case_index % len(difficulty_cycle)]
    guarantee_solvable = (case_index % 2) == 0

    random.seed(seed)
    np.random.seed(seed)

    context = ExpressionContext()
    expr = generate_random_expression(
        max_depth=max_depth,
        allow_calculus=True,
        allow_definite_integrals=True,
        max_derivative_order=2,
        difficulty=difficulty,
        guarantee_solvable=guarantee_solvable,
        generation_profile=generation_profile,
        context=context,
    )

    substitutions = context.substitutions.copy()
    substitutions.update(FUNCTIONS)
    options = EvaluatorOptions(
        calculator_mode=CalculatorModeOptions(enabled=calculator_mode_enabled)
    )

    answer, eval_context = evaluate(
        expr,
        substitutions=substitutions,
        error_on_invalid_snap=False,
        options=options,
    )

    return {
        "index": case_index + 1,
        "seed": seed,
        "difficulty": difficulty,
        "guarantee_solvable": guarantee_solvable,
        "expression_latex": _review_render(expr),
        "answer_latex": _review_render(answer),
        "solve_status": eval_context.solve_status,
        "reason_code": eval_context.reason_code,
        "is_approximate": eval_context.is_approximate,
        "explanation": eval_context.render(),
    }


def _render_markdown(cases: list[dict]) -> str:
    lines: list[str] = []
    lines.append("# Manual Verification Cases")
    lines.append("")
    lines.append(
        "Use this file to manually review generated problems, answers, and step-by-step explanations."
    )
    lines.append("")

    for case in cases:
        lines.append(
            f"## Case {case['index']} (seed={case['seed']}, difficulty={case['difficulty']}, guarantee_solvable={case['guarantee_solvable']})"
        )
        lines.append("")
        lines.append(f"- Problem: ${case['expression_latex']}$")
        lines.append(f"- Answer: ${case['answer_latex']}$")
        lines.append(
            f"- Solve status: `{case['solve_status']}` | reason_code: `{case['reason_code'] if case['reason_code'] is not None else '-'}` | approximate: `{case['is_approximate']}`"
        )
        lines.append("")
        lines.append(case["explanation"])
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a markdown file with problems, answers, and explanations for manual review."
    )
    parser.add_argument("--cases", type=int, default=40)
    parser.add_argument("--base-seed", type=int, default=17000)
    parser.add_argument("--max-depth", type=int, default=3)
    parser.add_argument(
        "--generation-profile",
        choices=["realistic", "stress"],
        default="realistic",
        help="Expression generation profile for manual-review cases.",
    )
    parser.add_argument(
        "--disable-calculator-mode",
        action="store_true",
        default=False,
        help="Disable calculator mode while generating manual-review explanations.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="manual_review_cases.md",
        help="Output markdown file path (relative to repo root or absolute path).",
    )
    args = parser.parse_args()

    cases: list[dict] = []
    for i in range(args.cases):
        cases.append(
            _build_case(
                i,
                args.base_seed,
                args.max_depth,
                args.generation_profile,
                calculator_mode_enabled=not args.disable_calculator_mode,
            )
        )

    output = Path(args.output)
    if not output.is_absolute():
        repo_root = Path(__file__).resolve().parents[1]
        output = repo_root / output

    output.write_text(_render_markdown(cases), encoding="utf-8")
    print(f"Wrote {len(cases)} cases to {output}")


if __name__ == "__main__":
    main()
