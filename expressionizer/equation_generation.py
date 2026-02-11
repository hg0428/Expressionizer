from __future__ import annotations

import random
from typing import Literal

from .expression import Equation, Symbol, SystemOfEquations, equation, power, product, sum


def _complexity_range(complexity: float | None = None) -> tuple[int, int]:
    if complexity is None:
        complexity = 0.5
    complexity = max(0.0, min(1.0, float(complexity)))
    bound = 9 + int(round(24 * complexity))
    return -bound, bound


def _nonzero_int(low: int, high: int) -> int:
    while True:
        value = random.randint(low, high)
        if value != 0:
            return value


def generate_linear_equation(
    complexity: float | None = None,
    variable_name: str = "x",
) -> tuple[Equation, list[Symbol]]:
    low, high = _complexity_range(complexity)
    variable = Symbol(variable_name)

    # Build ax + b = cx + d with a != c so there is a unique linear isolation target.
    a = _nonzero_int(low, high)
    c = _nonzero_int(low, high)
    while c == a:
        c = _nonzero_int(low, high)
    b = random.randint(low, high)
    d = random.randint(low, high)

    lhs = sum([product([a, variable]), b])
    rhs = sum([product([c, variable]), d])
    return equation(lhs, rhs), [variable]


def generate_quadratic_equation(
    complexity: float | None = None,
    variable_name: str = "x",
) -> tuple[Equation, list[Symbol]]:
    low, high = _complexity_range(complexity)
    variable = Symbol(variable_name)

    leading = _nonzero_int(low, high)
    r1 = random.randint(low, high)
    r2 = random.randint(low, high)

    lhs = product([leading, sum([variable, -r1]), sum([variable, -r2])])
    rhs = 0
    return equation(lhs, rhs), [variable]


def generate_rational_equation(
    complexity: float | None = None,
    variable_name: str = "x",
) -> tuple[Equation, list[Symbol]]:
    low, high = _complexity_range(complexity)
    variable = Symbol(variable_name)

    # (a*x + b)/x = c  ->  a*x + b = c*x  (linear after clearing denominator, x != 0)
    a = _nonzero_int(low, high)
    b = _nonzero_int(low, high)
    c = _nonzero_int(low, high)
    while c == a:
        c = _nonzero_int(low, high)

    lhs = product([sum([product([a, variable]), b]), power(variable, -1)])
    rhs = c
    return equation(lhs, rhs), [variable]


def generate_linear_system(
    complexity: float | None = None,
    size: int = 2,
) -> tuple[SystemOfEquations, list[Symbol]]:
    if size < 2:
        size = 2
    if size > 3:
        size = 3

    low, high = _complexity_range(complexity)
    variables = [Symbol(chr(ord("x") + i)) for i in range(size)]

    # Pick an integer solution first, then construct equations from random invertible matrix rows.
    target_values = [random.randint(low, high) for _ in range(size)]

    rows: list[list[int]] = []
    while len(rows) < size:
        row = [random.randint(low, high) for _ in range(size)]
        if all(v == 0 for v in row):
            continue
        if row not in rows:
            rows.append(row)

    # Basic invertibility checks for 2x2/3x3.
    if size == 2:
        while rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0] == 0:
            rows[1] = [random.randint(low, high) for _ in range(size)]
    elif size == 3:
        def _det3(m: list[list[int]]) -> int:
            return (
                m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
            )

        while _det3(rows) == 0:
            rows = [[random.randint(low, high) for _ in range(size)] for _ in range(size)]

    equations: list[Equation] = []
    for row in rows:
        lhs_terms = [product([coefficient, variable]) for coefficient, variable in zip(row, variables)]
        rhs = sum([coefficient * value for coefficient, value in zip(row, target_values)])
        equations.append(equation(sum(lhs_terms), rhs))

    return SystemOfEquations(equations), variables


def generate_random_equation_problem(
    complexity: float | None = None,
    mode: Literal["equation", "system", "mixed"] = "mixed",
    equation_families: list[str] | None = None,
) -> tuple[Equation | SystemOfEquations, list[Symbol], str]:
    if complexity is None:
        complexity = 0.5
    complexity = max(0.0, min(1.0, float(complexity)))
    valid_families = {"linear", "quadratic", "rational", "system"}
    allowed_families = set(valid_families)
    if equation_families:
        requested = {family.strip().lower() for family in equation_families if family.strip()}
        constrained = requested & valid_families
        if constrained:
            allowed_families = constrained

    if mode == "system":
        allowed_families = {"system"}
    elif mode == "equation":
        allowed_families = {name for name in allowed_families if name != "system"}
        if not allowed_families:
            allowed_families = {"linear", "quadratic", "rational"}

    choose_system = False
    if "system" in allowed_families:
        if mode == "system":
            choose_system = True
        elif mode == "mixed":
            choose_system = random.random() < 0.3
        elif allowed_families == {"system"}:
            choose_system = True

    if choose_system:
        size = 2 if complexity < 0.65 else (2 if random.random() < 0.5 else 3)
        system, variables = generate_linear_system(complexity=complexity, size=size)
        return system, variables, "system"

    rational_probability = 0.1 + 0.35 * complexity
    quadratic_probability = 0.15 + 0.45 * complexity
    linear_probability = max(0.05, 1.0 - rational_probability - quadratic_probability)

    candidates: list[tuple[str, float]] = []
    if "linear" in allowed_families:
        candidates.append(("linear", linear_probability))
    if "quadratic" in allowed_families:
        candidates.append(("quadratic", quadratic_probability))
    if "rational" in allowed_families:
        candidates.append(("rational", rational_probability))

    if not candidates:
        # Fallback to linear equation generation if families were constrained to empty equation set.
        candidates = [("linear", 1.0)]

    equation_family = random.choices(
        [name for name, _ in candidates],
        weights=[weight for _, weight in candidates],
        k=1,
    )[0]

    if equation_family == "rational":
        eq, variables = generate_rational_equation(complexity=complexity, variable_name="x")
        return eq, variables, "rational_equation"

    if equation_family == "quadratic":
        eq, variables = generate_quadratic_equation(complexity=complexity, variable_name="x")
        return eq, variables, "quadratic_equation"

    eq, variables = generate_linear_equation(complexity=complexity, variable_name="x")
    return eq, variables, "equation"
