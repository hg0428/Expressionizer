import argparse
import random
from pathlib import Path
from typing import Any

from .equation_generation import generate_random_equation_problem
from .localization import ExplanationProfile, Localizer, load_message_overrides
from .render import render_latex
from .solve_equation import EquationWordingOptions, solve_equation, solve_system


def _render_solution(values: dict[str, Any]) -> str:
    if not values:
        return "{}"
    rendered: list[str] = []
    for key in sorted(values):
        value = values[key]
        if isinstance(value, (int, float)):
            rendered_value = str(value)
        else:
            rendered_value = render_latex(value)
        rendered.append(f"{key}={rendered_value}")
    return "{ " + ", ".join(rendered) + " }"


def _build_case(
    case_index: int,
    base_seed: int,
    mode: str,
    step_heading_template: str,
    locale: str,
    style_type: str,
    message_overrides: dict[str, str],
    exact_text_overrides: dict[str, str],
) -> dict[str, Any]:
    difficulty_cycle = ["beginner", "intermediate", "advanced"]
    difficulty = difficulty_cycle[case_index % len(difficulty_cycle)]
    random.seed(base_seed + case_index)

    expr, variables, generated_kind = generate_random_equation_problem(
        difficulty=difficulty,
        mode=mode,
    )
    wording = EquationWordingOptions(
        step_heading_template=step_heading_template,
        explanation_profile=ExplanationProfile(
            locale=locale,
            style_type=style_type,
            message_overrides=message_overrides,
            exact_text_overrides=exact_text_overrides,
        ),
    )

    if generated_kind in ("equation", "quadratic_equation", "rational_equation"):
        solution, solve_context = solve_equation(
            expr,
            variable=variables[0],
            wording_options=wording,
        )
    else:
        solution, solve_context = solve_system(
            expr,
            variables=variables,
            wording_options=wording,
        )

    return {
        "index": case_index + 1,
        "seed": base_seed + case_index,
        "difficulty": difficulty,
        "kind": generated_kind,
        "problem_latex": render_latex(expr),
        "answer": _render_solution(solution.values),
        "solve_status": solution.status,
        "reason_code": solution.reason_code if solution.reason_code is not None else "-",
        "explanation": solve_context.render(),
    }


def _render_markdown(cases: list[dict[str, Any]], localizer: Localizer) -> str:
    lines: list[str] = []
    lines.append(localizer.template("equation_manual_review.title", "[[equation_manual_review.title]]"))
    lines.append("")
    lines.append(localizer.template("equation_manual_review.subtitle", "[[equation_manual_review.subtitle]]"))
    lines.append("")

    for case in cases:
        lines.append(
            localizer.format(
                "equation_manual_review.case_heading",
                "## [[equation_manual_review.case]] {index} (seed={seed}, difficulty={difficulty}, kind={kind})",
                {
                    "index": case["index"],
                    "seed": case["seed"],
                    "difficulty": case["difficulty"],
                    "kind": case["kind"],
                },
            )
        )
        lines.append("")
        lines.append(
            localizer.format(
                "equation_manual_review.problem",
                "- [[equation_manual_review.problem]]: ${problem}$",
                {"problem": case["problem_latex"]},
            )
        )
        lines.append(
            localizer.format(
                "equation_manual_review.solution",
                "- [[equation_manual_review.solution]]: `{solution}`",
                {"solution": case["answer"]},
            )
        )
        lines.append(
            localizer.format(
                "equation_manual_review.status",
                "- [[equation_manual_review.status]]: `{solve_status}` | [[equation_manual_review.reason_code]]: `{reason_code}`",
                {
                    "solve_status": case["solve_status"],
                    "reason_code": case["reason_code"],
                },
            )
        )
        lines.append("")
        lines.append(case["explanation"])
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate equation/system cases for manual explanation review."
    )
    parser.add_argument("--cases", type=int, default=40)
    parser.add_argument("--base-seed", type=int, default=22000)
    parser.add_argument(
        "--mode",
        choices=["linear", "quadratic", "rational", "system", "mixed"],
        default="mixed",
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
    parser.add_argument("--messages-file", type=str, default=None)
    parser.add_argument("--exact-text-overrides-file", type=str, default=None)
    parser.add_argument(
        "--output",
        type=str,
        default="equation_manual_review_cases.md",
        help="Output markdown path (repo-relative or absolute).",
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

    cases: list[dict[str, Any]] = []
    for index in range(args.cases):
        cases.append(
            _build_case(
                case_index=index,
                base_seed=args.base_seed,
                mode=args.mode,
                step_heading_template=args.step_heading_template,
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
    print(f"Wrote {len(cases)} equation review cases to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
