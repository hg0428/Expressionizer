from __future__ import annotations

import random
from typing import Literal

from .expression import Equation, Symbol, SystemOfEquations, equation, power, product, sum


def _difficulty_range(difficulty: str) -> tuple[int, int]:
    difficulty = (difficulty or "intermediate").lower()
    if difficulty == "beginner":
        return -9, 9
    if difficulty == "advanced":
        return -30, 30
    return -15, 15


def _nonzero_int(low: int, high: int) -> int:
    while True:
        value = random.randint(low, high)
        if value != 0:
            return value


def generate_linear_equation(
    difficulty: str = "intermediate",
    variable_name: str = "x",
) -> tuple[Equation, list[Symbol]]:
    low, high = _difficulty_range(difficulty)
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
    difficulty: str = "intermediate",
    variable_name: str = "x",
) -> tuple[Equation, list[Symbol]]:
    low, high = _difficulty_range(difficulty)
    variable = Symbol(variable_name)

    leading = _nonzero_int(low, high)
    r1 = random.randint(low, high)
    r2 = random.randint(low, high)

    lhs = product([leading, sum([variable, -r1]), sum([variable, -r2])])
    rhs = 0
    return equation(lhs, rhs), [variable]


def generate_rational_equation(
    difficulty: str = "intermediate",
    variable_name: str = "x",
) -> tuple[Equation, list[Symbol]]:
    low, high = _difficulty_range(difficulty)
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
    difficulty: str = "intermediate",
    size: int = 2,
) -> tuple[SystemOfEquations, list[Symbol]]:
    if size < 2:
        size = 2
    if size > 3:
        size = 3

    low, high = _difficulty_range(difficulty)
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
    difficulty: str = "intermediate",
    mode: Literal["equation", "system", "mixed"] = "mixed",
) -> tuple[Equation | SystemOfEquations, list[Symbol], str]:
    chosen_mode = mode
    if mode == "mixed":
        roll = random.random()
        if roll < 0.3:
            chosen_mode = "system"
        else:
            chosen_mode = "equation"

    if chosen_mode == "system":
        size = 2 if difficulty != "advanced" else (2 if random.random() < 0.65 else 3)
        system, variables = generate_linear_system(difficulty=difficulty, size=size)
        return system, variables, "system"

    equation_roll = random.random()
    rational_probability = 0.15 if difficulty == "beginner" else (0.25 if difficulty == "intermediate" else 0.35)
    quadratic_probability = 0.2 if difficulty == "beginner" else (0.35 if difficulty == "intermediate" else 0.5)

    if equation_roll < rational_probability:
        eq, variables = generate_rational_equation(difficulty=difficulty, variable_name="x")
        return eq, variables, "rational_equation"

    if equation_roll < (rational_probability + quadratic_probability):
        eq, variables = generate_quadratic_equation(difficulty=difficulty, variable_name="x")
        return eq, variables, "quadratic_equation"

    eq, variables = generate_linear_equation(difficulty=difficulty, variable_name="x")
    return eq, variables, "equation"
