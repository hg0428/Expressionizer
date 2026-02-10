from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
import re
from typing import Optional

from .expression import (
    Equation,
    FunctionCall,
    Integral,
    Power,
    Product,
    Sum,
    Symbol,
    SystemOfEquations,
    equation,
    is_int_or_float,
    power,
    product,
    sum as expr_sum,
)
from .render import render_latex


@dataclass
class EquationSolveContext:
    solve_status: str = "exact"
    reason_code: Optional[str] = None
    steps: list[str] = field(default_factory=list)
    step_heading_template: str = "## Step {number}"

    def add_step(self, text: str):
        self.steps.append(text)

    def set_status(self, solve_status: str, reason_code: Optional[str] = None):
        self.solve_status = solve_status
        self.reason_code = reason_code

    def render(self) -> str:
        if not self.steps:
            return ""
        lines: list[str] = []
        for index, step in enumerate(self.steps, 1):
            try:
                heading = self.step_heading_template.format(number=index)
            except Exception:
                heading = f"## Step {index}"
            lines.append(heading)
            lines.append(step)
            lines.append("")
        return "\n".join(lines).rstrip()


@dataclass
class EquationWordingOptions:
    step_heading_template: str = "## Step {number}"
    show_matrix_state: bool = True
    show_exact_and_approximate: bool = True


@dataclass
class EquationSolution:
    values: dict[str, object]
    status: str
    reason_code: Optional[str]


@dataclass
class _LinearForm:
    coefficients: dict[str, float]
    constant: float


@dataclass
class _PolynomialForm:
    coefficients: dict[int, float]


@dataclass
class _LaurentForm:
    coefficients: dict[int, float]


def _clean_number(value: float):
    if abs(value) < 1e-12:
        return 0
    rounded = round(value)
    if abs(value - rounded) < 1e-12:
        return int(rounded)
    return float(format(value, ".15g"))


def _to_fraction(value: float) -> Fraction:
    return Fraction(str(value)).limit_denominator(10**6)


def _fraction_to_latex(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    sign = "-" if value < 0 else ""
    magnitude = abs(value)
    return f"{sign}\\frac{{{magnitude.numerator}}}{{{magnitude.denominator}}}"


def _tidy_latex(text: str) -> str:
    # Normalize common artifacts like "a + -b" to "a - b" for paper-friendly output.
    cleaned = text
    cleaned = re.sub(r"\+\s*-\s*", "- ", cleaned)
    cleaned = re.sub(r"=\s*-\s*", "= -", cleaned)
    cleaned = re.sub(r"(?<![\d.])-1([A-Za-z])", r"-\1", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def _latex(expr) -> str:
    return _tidy_latex(render_latex(expr))


def _value_latex(value: object, show_exact_and_approximate: bool = True) -> str:
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        exact = _to_fraction(value)
        if exact.denominator == 1:
            return str(exact.numerator)
        exact_latex = _fraction_to_latex(exact)
        approximate = render_latex(_clean_number(value))
        if show_exact_and_approximate:
            return f"{exact_latex} \\approx {approximate}"
        return exact_latex
    return _latex(value)


def _matrix_latex(matrix: list[list[Fraction]], variable_names: list[str]) -> str:
    if not matrix:
        return "\\left[\\,\\right]"
    cols = len(variable_names)
    alignment = "c" * cols + "|c"
    rows: list[str] = []
    for row in matrix:
        entries = [_fraction_to_latex(row[col]) for col in range(cols)] + [
            _fraction_to_latex(row[cols])
        ]
        rows.append(" & ".join(entries))
    return "\\left[\\begin{array}{" + alignment + "}" + " \\\\ ".join(rows) + "\\end{array}\\right]"


def _collect_symbols(expr) -> set[str]:
    if isinstance(expr, Symbol):
        return {expr.name}
    if isinstance(expr, Sum):
        names: set[str] = set()
        for term in expr.terms:
            names.update(_collect_symbols(term))
        return names
    if isinstance(expr, Product):
        names: set[str] = set()
        for factor in expr.factors:
            names.update(_collect_symbols(factor))
        return names
    if isinstance(expr, Power):
        return _collect_symbols(expr.base).union(_collect_symbols(expr.exponent))
    if isinstance(expr, (FunctionCall, Integral)) or is_int_or_float(expr):
        return set()
    return set()


def _add_forms(left: _LinearForm, right: _LinearForm) -> _LinearForm:
    output: dict[str, float] = dict(left.coefficients)
    for name, value in right.coefficients.items():
        output[name] = output.get(name, 0.0) + value
        if abs(output[name]) < 1e-12:
            del output[name]
    return _LinearForm(output, left.constant + right.constant)


def _scale_form(form: _LinearForm, scale: float) -> _LinearForm:
    return _LinearForm(
        {name: value * scale for name, value in form.coefficients.items()},
        form.constant * scale,
    )


def _linearize(expr) -> tuple[bool, _LinearForm]:
    if isinstance(expr, bool):
        return False, _LinearForm({}, 0.0)
    if is_int_or_float(expr):
        return True, _LinearForm({}, float(expr))
    if isinstance(expr, Symbol):
        return True, _LinearForm({expr.name: 1.0}, 0.0)
    if isinstance(expr, Sum):
        output = _LinearForm({}, 0.0)
        for term in expr.terms:
            ok, partial = _linearize(term)
            if not ok:
                return False, _LinearForm({}, 0.0)
            output = _add_forms(output, partial)
        return True, output
    if isinstance(expr, Product):
        constant_factor = 1.0
        linear_part: Optional[_LinearForm] = None
        for factor in expr.factors:
            ok, partial = _linearize(factor)
            if not ok:
                return False, _LinearForm({}, 0.0)
            if partial.coefficients:
                if linear_part is not None:
                    return False, _LinearForm({}, 0.0)
                linear_part = partial
            else:
                constant_factor *= partial.constant
        if linear_part is None:
            return True, _LinearForm({}, constant_factor)
        return True, _scale_form(linear_part, constant_factor)
    if isinstance(expr, Power):
        if is_int_or_float(expr.exponent):
            exponent = float(expr.exponent)
            if abs(exponent) < 1e-12:
                return True, _LinearForm({}, 1.0)
            if abs(exponent - 1.0) < 1e-12:
                return _linearize(expr.base)
        return False, _LinearForm({}, 0.0)
    if isinstance(expr, (FunctionCall, Integral)):
        return False, _LinearForm({}, 0.0)
    return False, _LinearForm({}, 0.0)


def _form_to_expression(form: _LinearForm):
    terms = []
    for name in sorted(form.coefficients):
        coefficient = _clean_number(form.coefficients[name])
        variable = Symbol(name)
        if coefficient == 1:
            terms.append(variable)
        elif coefficient == -1:
            terms.append(product([-1, variable]))
        else:
            terms.append(product([coefficient, variable]))
    constant = _clean_number(form.constant)
    if constant != 0 or not terms:
        terms.append(constant)
    return expr_sum(terms)


def _build_rhs_for_variable(form: _LinearForm, variable_name: str):
    a = form.coefficients[variable_name]
    numerator_terms = [-form.constant]
    for name, value in sorted(form.coefficients.items()):
        if name == variable_name:
            continue
        numerator_terms.append(product([-value, Symbol(name)]))
    numerator = expr_sum(numerator_terms)
    denominator = _clean_number(a)
    if denominator == 1:
        return numerator
    return product([numerator, power(denominator, -1)])


def _poly_add(left: _PolynomialForm, right: _PolynomialForm) -> _PolynomialForm:
    output = dict(left.coefficients)
    for degree, value in right.coefficients.items():
        output[degree] = output.get(degree, 0.0) + value
        if abs(output[degree]) < 1e-12:
            del output[degree]
    return _PolynomialForm(output)


def _poly_scale(poly: _PolynomialForm, scalar: float) -> _PolynomialForm:
    return _PolynomialForm(
        {
            degree: coefficient * scalar
            for degree, coefficient in poly.coefficients.items()
        }
    )


def _laurent_add(left: _LaurentForm, right: _LaurentForm) -> _LaurentForm:
    output = dict(left.coefficients)
    for degree, value in right.coefficients.items():
        output[degree] = output.get(degree, 0.0) + value
        if abs(output[degree]) < 1e-12:
            del output[degree]
    return _LaurentForm(output)


def _laurent_mul(left: _LaurentForm, right: _LaurentForm) -> tuple[bool, _LaurentForm]:
    output: dict[int, float] = {}
    for d_left, v_left in left.coefficients.items():
        for d_right, v_right in right.coefficients.items():
            degree = d_left + d_right
            if degree < -1 or degree > 2:
                return False, _LaurentForm({})
            output[degree] = output.get(degree, 0.0) + (v_left * v_right)
    output = {degree: value for degree, value in output.items() if abs(value) >= 1e-12}
    return True, _LaurentForm(output)


def _laurent_scale(form: _LaurentForm, scalar: float) -> _LaurentForm:
    return _LaurentForm(
        {
            degree: coefficient * scalar
            for degree, coefficient in form.coefficients.items()
        }
    )


def _laurent_from_expr(expr, variable_name: str) -> tuple[bool, _LaurentForm]:
    if is_int_or_float(expr):
        return True, _LaurentForm({0: float(expr)})
    if isinstance(expr, Symbol):
        if expr.name != variable_name:
            return False, _LaurentForm({})
        return True, _LaurentForm({1: 1.0})
    if isinstance(expr, Sum):
        result = _LaurentForm({})
        for term in expr.terms:
            ok, part = _laurent_from_expr(term, variable_name)
            if not ok:
                return False, _LaurentForm({})
            result = _laurent_add(result, part)
        return True, result
    if isinstance(expr, Product):
        result = _LaurentForm({0: 1.0})
        for factor in expr.factors:
            ok, part = _laurent_from_expr(factor, variable_name)
            if not ok:
                return False, _LaurentForm({})
            ok, result = _laurent_mul(result, part)
            if not ok:
                return False, _LaurentForm({})
        return True, result
    if isinstance(expr, Power):
        if not is_int_or_float(expr.exponent):
            return False, _LaurentForm({})
        exponent = float(expr.exponent)
        if abs(exponent - round(exponent)) > 1e-12:
            return False, _LaurentForm({})
        exponent_int = int(round(exponent))
        if exponent_int == -1:
            if isinstance(expr.base, Symbol) and expr.base.name == variable_name:
                return True, _LaurentForm({-1: 1.0})
            return False, _LaurentForm({})
        if exponent_int < 0 or exponent_int > 2:
            return False, _LaurentForm({})
        if exponent_int == 0:
            return True, _LaurentForm({0: 1.0})
        ok, base = _laurent_from_expr(expr.base, variable_name)
        if not ok:
            return False, _LaurentForm({})
        result = _LaurentForm({0: 1.0})
        for _ in range(exponent_int):
            ok, result = _laurent_mul(result, base)
            if not ok:
                return False, _LaurentForm({})
        return True, result
    if isinstance(expr, (FunctionCall, Integral)):
        return False, _LaurentForm({})
    return False, _LaurentForm({})


def _poly_mul(left: _PolynomialForm, right: _PolynomialForm) -> tuple[bool, _PolynomialForm]:
    output: dict[int, float] = {}
    for d_left, v_left in left.coefficients.items():
        for d_right, v_right in right.coefficients.items():
            degree = d_left + d_right
            if degree > 2:
                return False, _PolynomialForm({})
            output[degree] = output.get(degree, 0.0) + (v_left * v_right)
    output = {degree: value for degree, value in output.items() if abs(value) >= 1e-12}
    return True, _PolynomialForm(output)


def _poly_from_expr(expr, variable_name: str) -> tuple[bool, _PolynomialForm]:
    if is_int_or_float(expr):
        return True, _PolynomialForm({0: float(expr)})
    if isinstance(expr, Symbol):
        if expr.name == variable_name:
            return True, _PolynomialForm({1: 1.0})
        return False, _PolynomialForm({})
    if isinstance(expr, Sum):
        result = _PolynomialForm({})
        for term in expr.terms:
            ok, poly = _poly_from_expr(term, variable_name)
            if not ok:
                return False, _PolynomialForm({})
            result = _poly_add(result, poly)
        return True, result
    if isinstance(expr, Product):
        result = _PolynomialForm({0: 1.0})
        for factor in expr.factors:
            ok, poly = _poly_from_expr(factor, variable_name)
            if not ok:
                return False, _PolynomialForm({})
            ok, result = _poly_mul(result, poly)
            if not ok:
                return False, _PolynomialForm({})
        return True, result
    if isinstance(expr, Power):
        if not is_int_or_float(expr.exponent):
            return False, _PolynomialForm({})
        exponent = float(expr.exponent)
        if abs(exponent - round(exponent)) > 1e-12:
            return False, _PolynomialForm({})
        exponent_int = int(round(exponent))
        if exponent_int < 0 or exponent_int > 2:
            return False, _PolynomialForm({})
        if exponent_int == 0:
            return True, _PolynomialForm({0: 1.0})
        ok, base_poly = _poly_from_expr(expr.base, variable_name)
        if not ok:
            return False, _PolynomialForm({})
        result = _PolynomialForm({0: 1.0})
        for _ in range(exponent_int):
            ok, result = _poly_mul(result, base_poly)
            if not ok:
                return False, _PolynomialForm({})
        return True, result
    if isinstance(expr, (FunctionCall, Integral)):
        return False, _PolynomialForm({})
    return False, _PolynomialForm({})


def _solve_quadratic_native(
    eq: Equation,
    variable_name: str,
    context: EquationSolveContext,
    wording_options: Optional[EquationWordingOptions] = None,
) -> Optional[EquationSolution]:
    lhs_poly_ok, lhs_poly = _poly_from_expr(eq.expressions[0], variable_name)
    rhs_poly_ok, rhs_poly = _poly_from_expr(eq.expressions[1], variable_name)
    if not lhs_poly_ok or not rhs_poly_ok:
        return None

    combined = _poly_add(lhs_poly, _poly_scale(rhs_poly, -1.0))
    if any(degree > 2 for degree in combined.coefficients):
        return None
    if 2 not in combined.coefficients:
        return None

    a = combined.coefficients.get(2, 0.0)
    b = combined.coefficients.get(1, 0.0)
    c = combined.coefficients.get(0, 0.0)
    if abs(a) < 1e-12:
        return None

    x = Symbol(variable_name)
    canonical = equation(
        expr_sum(
            [
                product([_clean_number(a), power(x, 2)]),
                product([_clean_number(b), x]),
                _clean_number(c),
            ]
        ),
        0,
    )
    context.add_step(f"Rearrange into quadratic form: $$ {_latex(canonical)} $$")

    discriminant = b * b - 4 * a * c
    context.add_step(
        "Compute the discriminant: "
        + f"$$\\Delta = b^2 - 4ac = {_latex(_clean_number(discriminant))}$$"
    )

    if discriminant < -1e-12:
        context.set_status("unsolved", "no_real_solution")
        context.add_step("The discriminant is negative, so there are no real solutions.")
        return EquationSolution({}, context.solve_status, context.reason_code)

    if abs(discriminant) <= 1e-12:
        root = _clean_number((-b) / (2 * a))
        context.add_step(
            "Use the quadratic formula with $\\Delta = 0$ to get one repeated root: "
            + f"$$ {variable_name} = {_value_latex(root, (wording_options.show_exact_and_approximate if wording_options else True))} $$"
        )
        return EquationSolution({variable_name: root}, context.solve_status, context.reason_code)

    sqrt_discriminant = discriminant ** 0.5
    root_1 = _clean_number(((-b) + sqrt_discriminant) / (2 * a))
    root_2 = _clean_number(((-b) - sqrt_discriminant) / (2 * a))
    roots = sorted([root_1, root_2], key=lambda value: float(value))
    context.add_step(
        "Apply the quadratic formula: "
        + f"$$ {variable_name} = \\frac{{-b \\pm \\sqrt{{\\Delta}}}}{{2a}} $$"
    )
    context.add_step(
        f"Therefore, $$ {variable_name} \\in \\{{{_value_latex(roots[0], (wording_options.show_exact_and_approximate if wording_options else True))}, {_value_latex(roots[1], (wording_options.show_exact_and_approximate if wording_options else True))}\\}} $$"
    )
    return EquationSolution({variable_name: roots}, context.solve_status, context.reason_code)


def _solve_rational_native(
    eq: Equation,
    variable_name: str,
    context: EquationSolveContext,
    wording_options: Optional[EquationWordingOptions] = None,
) -> Optional[EquationSolution]:
    lhs_ok, lhs = _laurent_from_expr(eq.expressions[0], variable_name)
    rhs_ok, rhs = _laurent_from_expr(eq.expressions[1], variable_name)
    if not lhs_ok or not rhs_ok:
        return None

    combined = _laurent_add(lhs, _laurent_scale(rhs, -1.0))
    if not combined.coefficients:
        context.set_status("partial", "infinite_solutions")
        context.add_step("The equation simplifies to an identity on the allowed domain.")
        return EquationSolution({}, context.solve_status, context.reason_code)

    min_degree = min(combined.coefficients)
    max_degree = max(combined.coefficients)
    if min_degree != -1 or max_degree > 1:
        return None

    x = Symbol(variable_name)
    context.add_step(
        f"Domain restriction: ${variable_name} \\neq 0$ because it appears in a denominator."
    )
    context.add_step(
        f"Multiply both sides by ${variable_name}$ to clear the denominator."
    )

    shifted: dict[int, float] = {}
    for degree, coefficient in combined.coefficients.items():
        shifted_degree = degree + 1
        shifted[shifted_degree] = shifted.get(shifted_degree, 0.0) + coefficient

    a2 = shifted.get(2, 0.0)
    a1 = shifted.get(1, 0.0)
    a0 = shifted.get(0, 0.0)
    canonical = equation(
        expr_sum(
            [
                product([_clean_number(a2), power(x, 2)]),
                product([_clean_number(a1), x]),
                _clean_number(a0),
            ]
        ),
        0,
    )
    context.add_step(f"After clearing denominators: $$ {_latex(canonical)} $$")

    if abs(a2) < 1e-12 and abs(a1) < 1e-12:
        context.set_status("unsolved", "no_solution")
        context.add_step("The reduced equation is inconsistent, so there is no solution.")
        return EquationSolution({}, context.solve_status, context.reason_code)

    candidate_values: list[float] = []
    if abs(a2) < 1e-12:
        root = (-a0) / a1
        candidate_values = [root]
        context.add_step(
            f"Solve the linear equation: $$ {variable_name} = {_value_latex(_clean_number(root), (wording_options.show_exact_and_approximate if wording_options else True))} $$"
        )
    else:
        discriminant = a1 * a1 - 4 * a2 * a0
        context.add_step(
            "Compute the discriminant: "
            + f"$$\\Delta = {render_latex(_clean_number(discriminant))}$$"
        )
        if discriminant < -1e-12:
            context.set_status("unsolved", "no_real_solution")
            context.add_step("The discriminant is negative, so there are no real solutions.")
            return EquationSolution({}, context.solve_status, context.reason_code)
        if abs(discriminant) <= 1e-12:
            candidate_values = [(-a1) / (2 * a2)]
        else:
            sqrt_discriminant = discriminant ** 0.5
            candidate_values = [
                ((-a1) + sqrt_discriminant) / (2 * a2),
                ((-a1) - sqrt_discriminant) / (2 * a2),
            ]

    filtered = []
    for value in candidate_values:
        if abs(value) > 1e-12:
            cleaned = _clean_number(value)
            if cleaned not in filtered:
                filtered.append(cleaned)

    if not filtered:
        context.set_status("unsolved", "no_solution_domain_restriction")
        context.add_step(
            f"All candidate roots violate the domain restriction ${variable_name} \\neq 0$."
        )
        return EquationSolution({}, context.solve_status, context.reason_code)

    if len(filtered) == 1:
        context.add_step(
            f"Valid solution after domain check: $$ {variable_name} = {_value_latex(filtered[0], (wording_options.show_exact_and_approximate if wording_options else True))} $$"
        )
        return EquationSolution({variable_name: filtered[0]}, context.solve_status, context.reason_code)

    filtered.sort(key=lambda value: float(value))
    context.add_step(
        "Valid solutions after domain check: "
        + f"$$ {variable_name} \\in \\{{{_value_latex(filtered[0], (wording_options.show_exact_and_approximate if wording_options else True))}, {_value_latex(filtered[1], (wording_options.show_exact_and_approximate if wording_options else True))}\\}} $$"
    )
    return EquationSolution({variable_name: filtered}, context.solve_status, context.reason_code)


def solve_equation(
    eq: Equation,
    variable: Optional[Symbol | str] = None,
    wording_options: Optional[EquationWordingOptions] = None,
) -> tuple[EquationSolution, EquationSolveContext]:
    context = EquationSolveContext(
        step_heading_template=(
            wording_options.step_heading_template
            if wording_options is not None
            else "## Step {number}"
        )
    )
    context.add_step(f"Solve the equation: $${_latex(eq)}$$")

    if len(eq.expressions) != 2:
        context.set_status("unsolved", "unsupported_equation_arity")
        context.add_step("Only two-sided equations are supported in this solver.")
        return EquationSolution({}, context.solve_status, context.reason_code), context

    lhs, rhs = eq.expressions
    lhs_ok, lhs_form = _linearize(lhs)
    rhs_ok, rhs_form = _linearize(rhs)
    if not lhs_ok or not rhs_ok:
        variable_name = variable.name if isinstance(variable, Symbol) else variable
        if variable_name is None:
            symbols = _collect_symbols(lhs).union(_collect_symbols(rhs))
            if len(symbols) == 1:
                variable_name = next(iter(symbols))
        if variable_name is None:
            context.set_status("partial", "multiple_variables")
            context.add_step(
                "Nonlinear native solving requires a single target variable. Pass `variable=` explicitly."
            )
            return EquationSolution({}, context.solve_status, context.reason_code), context
        rational_solution = _solve_rational_native(
            eq,
            variable_name,
            context,
            wording_options=wording_options,
        )
        if rational_solution is not None:
            return rational_solution, context
        quadratic_solution = _solve_quadratic_native(
            eq,
            variable_name,
            context,
            wording_options=wording_options,
        )
        if quadratic_solution is not None:
            return quadratic_solution, context
        context.set_status("partial", "nonlinear_unsupported_native_only")
        context.add_step(
            "This nonlinear equation is outside native-supported patterns, so it is left unsolved."
        )
        return EquationSolution({}, context.solve_status, context.reason_code), context

    combined = _add_forms(lhs_form, _scale_form(rhs_form, -1.0))
    canonical_equation = equation(_form_to_expression(combined), 0)
    context.add_step(
        "Subtract the right-hand side from both sides to write the equation in standard form: "
        + f"$$ {_latex(canonical_equation)} $$"
    )

    variable_name = variable.name if isinstance(variable, Symbol) else variable
    nonzero_variables = [
        name for name, value in combined.coefficients.items() if abs(value) > 1e-12
    ]

    if len(nonzero_variables) == 0:
        if abs(combined.constant) < 1e-12:
            context.set_status("partial", "infinite_solutions")
            context.add_step("The equation simplifies to $0 = 0$, so infinitely many solutions exist.")
        else:
            context.set_status("unsolved", "no_solution")
            context.add_step("The equation simplifies to a contradiction, so there is no solution.")
        return EquationSolution({}, context.solve_status, context.reason_code), context

    if variable_name is None:
        if len(nonzero_variables) == 1:
            variable_name = nonzero_variables[0]
        else:
            context.set_status("partial", "multiple_variables")
            context.add_step(
                "Multiple variables remain. Pass `variable=` to solve for a specific one."
            )
            return EquationSolution({}, context.solve_status, context.reason_code), context

    if variable_name not in combined.coefficients:
        context.set_status("partial", "target_variable_missing")
        context.add_step(f"No term with ${variable_name}$ appears after simplification.")
        return EquationSolution({}, context.solve_status, context.reason_code), context

    coefficient = combined.coefficients[variable_name]
    if abs(coefficient) < 1e-12:
        context.set_status("partial", "zero_target_coefficient")
        context.add_step(
            f"The coefficient of ${variable_name}$ is 0, so direct isolation is not possible."
        )
        return EquationSolution({}, context.solve_status, context.reason_code), context

    rhs_expression = _build_rhs_for_variable(combined, variable_name)
    isolated = equation(Symbol(variable_name), rhs_expression)
    if len(nonzero_variables) == 1:
        constant_term = _clean_number(combined.constant)
        coefficient_term = _clean_number(coefficient)
        if constant_term != 0:
            reduced_equation = equation(
                product([coefficient_term, Symbol(variable_name)]),
                _clean_number(-constant_term),
            )
            context.add_step(
                f"Add ${_latex(-constant_term)}$ to both sides to isolate the variable term: "
                + f"$$ {_latex(reduced_equation)} $$"
            )
        if coefficient_term != 1:
            context.add_step(
                f"Divide both sides by ${_latex(coefficient_term)}$."
            )
    context.add_step(f"Isolate ${variable_name}$: $$ {_latex(isolated)} $$")

    if len(nonzero_variables) == 1:
        numeric_value = _clean_number(float(-combined.constant / coefficient))
        context.add_step(
            "Therefore, "
            + f"$$ {variable_name} = {_value_latex(numeric_value, (wording_options.show_exact_and_approximate if wording_options else True))} $$"
        )
        return (
            EquationSolution({variable_name: numeric_value}, context.solve_status, context.reason_code),
            context,
        )

    context.set_status("partial", "symbolic_solution_with_free_variables")
    return (
        EquationSolution({variable_name: rhs_expression}, context.solve_status, context.reason_code),
        context,
    )


def solve_system(
    system: SystemOfEquations | list[Equation],
    variables: Optional[list[Symbol | str]] = None,
    tolerance: float = 1e-10,
    wording_options: Optional[EquationWordingOptions] = None,
) -> tuple[EquationSolution, EquationSolveContext]:
    context = EquationSolveContext(
        step_heading_template=(
            wording_options.step_heading_template
            if wording_options is not None
            else "## Step {number}"
        )
    )
    equations = system.equations if isinstance(system, SystemOfEquations) else system
    context.add_step(
        "Solve the system:\n$$"
        + "\\left\\{\\begin{array}{l}"
        + " \\\\ ".join(_latex(eq) for eq in equations)
        + "\\end{array}\\right."
        + "$$"
    )

    if not equations:
        context.set_status("partial", "empty_system")
        context.add_step("No equations were provided.")
        return EquationSolution({}, context.solve_status, context.reason_code), context

    forms: list[_LinearForm] = []
    for eq in equations:
        if len(eq.expressions) != 2:
            context.set_status("unsolved", "unsupported_equation_arity")
            context.add_step("Each equation must have exactly two sides.")
            return EquationSolution({}, context.solve_status, context.reason_code), context
        lhs_ok, lhs_form = _linearize(eq.expressions[0])
        rhs_ok, rhs_form = _linearize(eq.expressions[1])
        if not lhs_ok or not rhs_ok:
            context.set_status("partial", "nonlinear_or_unsupported_terms")
            context.add_step("At least one equation is nonlinear or unsupported.")
            return EquationSolution({}, context.solve_status, context.reason_code), context
        forms.append(_add_forms(lhs_form, _scale_form(rhs_form, -1.0)))

    if variables is None:
        names: set[str] = set()
        for form in forms:
            names.update(name for name, value in form.coefficients.items() if abs(value) > tolerance)
        variable_names = sorted(names)
    else:
        variable_names = [
            variable.name if isinstance(variable, Symbol) else variable for variable in variables
        ]
    if not variable_names:
        context.set_status("partial", "no_variables")
        context.add_step("The system has no variables after simplification.")
        return EquationSolution({}, context.solve_status, context.reason_code), context

    matrix: list[list[Fraction]] = []
    for form in forms:
        row = [_to_fraction(form.coefficients.get(name, 0.0)) for name in variable_names]
        rhs = _to_fraction(-form.constant)
        matrix.append(row + [rhs])

    rows = len(matrix)
    cols = len(variable_names)
    if wording_options is None or wording_options.show_matrix_state:
        context.add_step(
            "Write the augmented matrix:\n"
            + f"$${_matrix_latex(matrix, variable_names)}$$"
        )
    pivot_row = 0
    pivot_columns: list[int] = []

    for col in range(cols):
        candidate = None
        best_abs = 0.0
        for row in range(pivot_row, rows):
            value = abs(float(matrix[row][col]))
            if value > best_abs + tolerance:
                best_abs = value
                candidate = row
        if candidate is None or best_abs <= tolerance:
            continue
        if candidate != pivot_row:
            matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]
            step = f"Swap row {pivot_row + 1} with row {candidate + 1}."
            if wording_options is None or wording_options.show_matrix_state:
                step += "\n" + f"$${_matrix_latex(matrix, variable_names)}$$"
            context.add_step(step)
        pivot = matrix[pivot_row][col]
        if abs(float(pivot)) > tolerance and pivot != 1:
            for j in range(col, cols + 1):
                matrix[pivot_row][j] /= pivot
            step = (
                f"Normalize row {pivot_row + 1} by dividing by ${_fraction_to_latex(pivot)}$."
            )
            if wording_options is None or wording_options.show_matrix_state:
                step += "\n" + f"$${_matrix_latex(matrix, variable_names)}$$"
            context.add_step(step)
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = matrix[row][col]
            if abs(float(factor)) <= tolerance:
                continue
            for j in range(col, cols + 1):
                matrix[row][j] -= factor * matrix[pivot_row][j]
            step = (
                f"Eliminate column {col + 1} in row {row + 1} using factor ${_fraction_to_latex(factor)}$."
            )
            if wording_options is None or wording_options.show_matrix_state:
                step += "\n" + f"$${_matrix_latex(matrix, variable_names)}$$"
            context.add_step(step)
        pivot_columns.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break

    for row in range(rows):
        lhs_norm = sum(abs(float(matrix[row][col])) for col in range(cols))
        if lhs_norm <= tolerance and abs(float(matrix[row][cols])) > tolerance:
            context.set_status("unsolved", "no_solution")
            context.add_step("A row reduced to $0 = c$ with $c \\neq 0$, so the system is inconsistent.")
            return EquationSolution({}, context.solve_status, context.reason_code), context

    if len(pivot_columns) < cols:
        context.set_status("partial", "infinite_solutions")
        context.add_step("Not every variable has a pivot; the system has infinitely many solutions.")
        return EquationSolution({}, context.solve_status, context.reason_code), context

    values: dict[str, object] = {}
    for row, col in enumerate(pivot_columns):
        values[variable_names[col]] = _clean_number(float(matrix[row][cols]))
    solution_display = ", ".join(
        f"{name} = {_value_latex(value, (wording_options.show_exact_and_approximate if wording_options else True))}"
        for name, value in sorted(values.items())
    )
    context.add_step(f"Unique solution found: $$ {solution_display} $$")
    return EquationSolution(values, context.solve_status, context.reason_code), context
