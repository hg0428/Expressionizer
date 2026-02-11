import argparse
import math
import random
from pathlib import Path

import numpy as np

from .evaluator import CalculatorModeOptions, EvaluatorOptions, evaluate
from .localization import ExplanationProfile, Localizer, load_message_overrides
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
    solvability_mode: str,
    unsolvable_probability: float,
    hard_problem_probability: float,
    locale: str,
    style_type: str,
    message_overrides: dict[str, str],
    exact_text_overrides: dict[str, str],
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
        solvability_mode=solvability_mode,
        unsolvable_probability=unsolvable_probability,
        hard_problem_probability=hard_problem_probability,
        context=context,
    )

    substitutions = context.substitutions.copy()
    substitutions.update(FUNCTIONS)
    options = EvaluatorOptions(
        calculator_mode=CalculatorModeOptions(enabled=calculator_mode_enabled),
        explanation_profile=ExplanationProfile(
            locale=locale,
            style_type=style_type,
            message_overrides=message_overrides,
            exact_text_overrides=exact_text_overrides,
        ),
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


def _render_markdown(cases: list[dict], localizer: Localizer) -> str:
    lines: list[str] = []
    lines.append(localizer.template("manual_review.title", "[[manual_review.title]]"))
    lines.append("")
    lines.append(localizer.template("manual_review.subtitle", "[[manual_review.subtitle]]"))
    lines.append("")

    for case in cases:
        lines.append(
            localizer.format(
                "manual_review.case_heading",
                "## [[manual_review.case]] {index} (seed={seed}, difficulty={difficulty}, guarantee_solvable={guarantee_solvable})",
                {
                    "index": case["index"],
                    "seed": case["seed"],
                    "difficulty": case["difficulty"],
                    "guarantee_solvable": case["guarantee_solvable"],
                },
            )
        )
        lines.append("")
        lines.append(
            localizer.format(
                "manual_review.problem",
                "- [[manual_review.problem]]: ${expression}$",
                {"expression": case["expression_latex"]},
            )
        )
        lines.append(
            localizer.format(
                "manual_review.answer",
                "- [[manual_review.answer]]: ${answer}$",
                {"answer": case["answer_latex"]},
            )
        )
        lines.append(
            localizer.format(
                "manual_review.status",
                "- [[manual_review.status]]: `{solve_status}` | [[manual_review.reason_code]]: `{reason_code}` | [[manual_review.approximate]]: `{approximate}`",
                {
                    "solve_status": case["solve_status"],
                    "reason_code": case["reason_code"] if case["reason_code"] is not None else "-",
                    "approximate": case["is_approximate"],
                },
            )
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
        "--solvability-mode",
        choices=["mixed", "solvable", "unsolvable"],
        default="mixed",
        help="Control whether generated cases include intentionally unsolvable problems.",
    )
    parser.add_argument(
        "--unsolvable-probability",
        type=float,
        default=0.12,
        help="When solvability-mode=mixed, probability of intentionally unsolvable cases.",
    )
    parser.add_argument(
        "--hard-problem-probability",
        type=float,
        default=0.2,
        help="Probability of promoting a realistic case to a harder variant.",
    )
    parser.add_argument(
        "--disable-calculator-mode",
        action="store_true",
        default=False,
        help="Disable calculator mode while generating manual-review explanations.",
    )
    parser.add_argument("--locale", type=str, default="en")
    parser.add_argument(
        "--style-type",
        choices=["default", "compact", "plain", "xml"],
        default="default",
    )
    parser.add_argument("--messages-file", type=str, default=None)
    parser.add_argument("--exact-text-overrides-file", type=str, default=None)
    parser.add_argument(
        "--output",
        type=str,
        default="manual_review_cases.md",
        help="Output markdown file path (relative to repo root or absolute path).",
    )
    args = parser.parse_args()
    message_overrides = (
        load_message_overrides(args.messages_file) if args.messages_file else {}
    )
    exact_text_overrides = (
        load_message_overrides(args.exact_text_overrides_file)
        if args.exact_text_overrides_file
        else {}
    )

    cases: list[dict] = []
    for i in range(args.cases):
        cases.append(
            _build_case(
                i,
                args.base_seed,
                args.max_depth,
                args.generation_profile,
                calculator_mode_enabled=not args.disable_calculator_mode,
                solvability_mode=args.solvability_mode,
                unsolvable_probability=args.unsolvable_probability,
                hard_problem_probability=args.hard_problem_probability,
                locale=args.locale,
                style_type=args.style_type,
                message_overrides=message_overrides,
                exact_text_overrides=exact_text_overrides,
            )
        )

    output = Path(args.output)
    if not output.is_absolute():
        repo_root = Path(__file__).resolve().parents[1]
        output = repo_root / output

    localizer = Localizer.from_profile(
        ExplanationProfile(
            locale=args.locale,
            style_type=args.style_type,
            message_overrides=message_overrides,
            exact_text_overrides=exact_text_overrides,
        )
    )
    output.write_text(_render_markdown(cases, localizer), encoding="utf-8")
    print(f"Wrote {len(cases)} cases to {output}")


if __name__ == "__main__":
    main()
