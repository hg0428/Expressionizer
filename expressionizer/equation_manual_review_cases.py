import argparse
import random
from pathlib import Path
from typing import Any, Optional

from .equation_generation import generate_random_equation_problem
from .localization import (
    Localizer,
    build_explanation_profile,
    load_message_overrides,
    supported_profile_presets,
)
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
    profile_preset: Optional[str],
    collect_localization_diagnostics: bool,
    equation_families: Optional[list[str]],
    message_overrides: dict[str, str],
    exact_text_overrides: dict[str, str],
) -> dict[str, Any]:
    complexity_cycle = [0.2, 0.5, 0.8]
    complexity = complexity_cycle[case_index % len(complexity_cycle)]
    random.seed(base_seed + case_index)

    generator_mode = mode
    if mode in ("linear", "quadratic", "rational"):
        generator_mode = "equation"
        equation_families = [mode]
    expr, variables, generated_kind = generate_random_equation_problem(
        complexity=complexity,
        mode=generator_mode,
        equation_families=equation_families,
    )
    wording = EquationWordingOptions(
        step_heading_template=step_heading_template,
        explanation_profile=build_explanation_profile(
            profile_preset,
            locale=locale,
            style_type=style_type,
            message_overrides=message_overrides,
            exact_text_overrides=exact_text_overrides,
            collect_diagnostics=collect_localization_diagnostics,
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
        "complexity": complexity,
        "kind": generated_kind,
        "problem_latex": render_latex(expr),
        "answer": _render_solution(solution.values),
        "solve_status": solution.status,
        "reason_code": solution.reason_code if solution.reason_code is not None else "-",
        "localization_diagnostics": solve_context.localizer.diagnostics()
        if solve_context.localizer is not None
        else {},
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
                "## [[equation_manual_review.case]] {index} (seed={seed}, complexity={complexity}, kind={kind})",
                {
                    "index": case["index"],
                    "seed": case["seed"],
                    "complexity": case["complexity"],
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
        "--equation-families",
        type=lambda s: [p.strip() for p in s.split(",") if p.strip()],
        default=None,
        help="Comma-separated equation families: linear,quadratic,rational,system",
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
                profile_preset=args.profile_preset,
                collect_localization_diagnostics=args.collect_localization_diagnostics,
                equation_families=args.equation_families,
                message_overrides=message_overrides,
                exact_text_overrides=exact_text_overrides,
            )
        )

    output = Path(args.output)
    if not output.is_absolute():
        repo_root = Path(__file__).resolve().parents[1]
        output = repo_root / output

    localizer = Localizer.from_profile(
        build_explanation_profile(
            args.profile_preset,
            locale=args.locale,
            style_type=args.style_type,
            message_overrides=message_overrides,
            exact_text_overrides=exact_text_overrides,
            collect_diagnostics=args.collect_localization_diagnostics,
        )
    )
    output.write_text(_render_markdown(cases, localizer), encoding="utf-8")
    print(f"Wrote {len(cases)} equation review cases to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
