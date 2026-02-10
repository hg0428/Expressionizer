import argparse
import random
from pathlib import Path
from typing import Any

from .equation_generation import generate_random_equation_problem
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
) -> dict[str, Any]:
    difficulty_cycle = ["beginner", "intermediate", "advanced"]
    difficulty = difficulty_cycle[case_index % len(difficulty_cycle)]
    random.seed(base_seed + case_index)

    expr, variables, generated_kind = generate_random_equation_problem(
        difficulty=difficulty,
        mode=mode,
    )
    wording = EquationWordingOptions(step_heading_template=step_heading_template)

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


def _render_markdown(cases: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# Equation Manual Verification Cases")
    lines.append("")
    lines.append("Generated equation/system problems with native step-by-step solutions.")
    lines.append("")

    for case in cases:
        lines.append(
            "## Case "
            + f"{case['index']} (seed={case['seed']}, difficulty={case['difficulty']}, kind={case['kind']})"
        )
        lines.append("")
        lines.append(f"- Problem: ${case['problem_latex']}$")
        lines.append(f"- Solution: `{case['answer']}`")
        lines.append(
            f"- Solve status: `{case['solve_status']}` | reason_code: `{case['reason_code']}`"
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
        default="## Step {number}",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="equation_manual_review_cases.md",
        help="Output markdown path (repo-relative or absolute).",
    )
    args = parser.parse_args()

    cases: list[dict[str, Any]] = []
    for index in range(args.cases):
        cases.append(
            _build_case(
                case_index=index,
                base_seed=args.base_seed,
                mode=args.mode,
                step_heading_template=args.step_heading_template,
            )
        )

    output = Path(args.output)
    if not output.is_absolute():
        repo_root = Path(__file__).resolve().parents[1]
        output = repo_root / output

    output.write_text(_render_markdown(cases), encoding="utf-8")
    print(f"Wrote {len(cases)} equation review cases to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
