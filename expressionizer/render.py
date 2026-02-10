import math
from numbers import Real
from .expression import *
from .number_format import to_trimmed_decimal_string


@dataclass
class LaTeXRenderOptions:
    group_exponentiation: bool = (
        False  # Always add a group around exponentiation, even when it is otherwise clear.
    )
    parentheses_function_call: bool = False  # Use parentheses rather than {}
    backslash_function_call: bool = True  # Put a backslash before the function call
    product_separator: str = (
        ""  # Default product separator for cases when it is clear either way.
    )
    always_use_product_parentheses = False  # Always used parentheses around factors in a product, even if it is clear otherwise
    use_parentheses_for_literal_product = (
        True  # Use parentheses rather than \cdot when multiplying literals
    )
    group_on_one_argument_function: bool = (
        True  # Do you need the grouping ({} or ()) if it only has one argument
    )
    fraction_as_inline: bool = False  # \frac vs just using /
    negative_exponent_as_fraction: bool = (
        True  # Convert negative exponents to fractions.
    )
    compact_exponents: bool = (
        True  # In cases where it is clear either way, compact_exponents will use x^y instead of x^{y}
    )


def apply_group(text, paren=False, square=False, curly=False):
    if paren:
        return "(" + text + ")"
    elif square:
        return "[" + text + "]"
    elif curly:
        return "{" + text + "}"
    else:
        return text


def _split_signed_term(term):
    if isinstance(term, Real) and not isinstance(term, bool):
        if float(term) < 0:
            return True, -term
        return False, term
    if isinstance(term, Product) and len(term.factors) > 0:
        first = term.factors[0]
        if isinstance(first, Real) and not isinstance(first, bool) and float(first) < 0:
            abs_first = -first
            remaining = list(term.factors[1:])
            if abs_first == 1 and remaining:
                if len(remaining) == 1:
                    return True, remaining[0]
                return True, product(remaining)
            return True, product([abs_first] + remaining)
    return False, term


def _render_sum_with_signs(
    terms: list[Numerical],
    renderer,
    group: bool = False,
    apply_group_fn=None,
    paren_group: bool = False,
    square_group: bool = False,
    curly_group: bool = False,
):
    flattened_terms = []

    def _flatten(term):
        if isinstance(term, Sum):
            for nested in term.terms:
                _flatten(nested)
        else:
            flattened_terms.append(term)

    for term in terms:
        _flatten(term)

    if len(flattened_terms) == 0:
        rendered = "0"
    else:
        parts: list[str] = []
        for index, term in enumerate(flattened_terms):
            rendered_term = renderer(term)
            is_negative = rendered_term.startswith("-")
            if is_negative:
                abs_rendered = rendered_term[1:].lstrip()
            else:
                # Fallback to structural sign detection in case renderer did not include
                # a literal leading '-' for a negative term representation.
                structural_negative, abs_term = _split_signed_term(term)
                is_negative = structural_negative
                abs_rendered = renderer(abs_term)
            if index == 0:
                parts.append(("-" if is_negative else "") + abs_rendered)
            else:
                parts.append((" - " if is_negative else " + ") + abs_rendered)
        rendered = "".join(parts)
    if apply_group_fn is not None:
        return apply_group_fn(rendered, paren_group, square_group, curly_group)
    if group and len(flattened_terms) > 1:
        return "(" + rendered + ")"
    return rendered


def render(expression: Union[Numerical, Equation, InEquality, SystemOfEquations], group=False):
    match expression:
        case int() | float():
            if expression == math.pi:
                return "π"
            return to_trimmed_decimal_string(expression)
        case Power(base, exponent) if (
            isinstance(expression.exponent, int)
            or isinstance(expression.exponent, float)
        ) and exponent < 0:
            output = f"1/{render(power(base, -exponent), True)}"
            if group:
                return "(" + output + ")"
            else:
                return output
        case Power(value, Power(base, exponent)) if (
            (isinstance(exponent, int) or isinstance(exponent, float))
            and isinstance(base, (int, float))
            and exponent < 0
        ):
            # Root
            root = base ** (-exponent)
            if root == 2:
                return f"sqrt({render(value)})"
            else:
                return f"root({render(value, True)}, {root})"

        case Power():
            output = (
                f"{render(expression.base, True)}^{render(expression.exponent, True)}"
            )
            if group:
                return apply_group(output, True)
            else:
                return output
        case Product():
            positive_exponents = []
            negative_exponents = []
            for factor in expression.factors:
                match factor:
                    case Power(base, exponent) if (
                        isinstance(exponent, int) or isinstance(exponent, float)
                    ) and exponent < 0:
                        negative_exponents.append(power(base, -exponent))
                    case _:
                        positive_exponents.append(factor)
            if len(negative_exponents) > 0:
                output = f"{render(product(positive_exponents), True)}/{render(product(negative_exponents), True)}"
                if group:
                    return "(" + output + ")"
                else:
                    return output
            else:
                return "".join(
                    map(lambda factor: render(factor, True), expression.factors)
                )
        case Sum():
            return _render_sum_with_signs(
                expression.terms,
                renderer=lambda term: render(term),
                group=group,
            )
        case FunctionCall():
            if len(expression.subscript_arguments) == 0:
                subscript = ""
            elif len(expression.subscript_arguments) == 1:
                subscript = f"_{", ".join(map(repr, expression.subscript_arguments))}"
            else:
                subscript = (
                    f"_{{{', '.join(map(repr, expression.subscript_arguments))}}}"
                )

            if len(expression.superscript_arguments) == 0:
                superscript = ""
            elif len(expression.superscript_arguments) == 1:
                superscript = (
                    f"^{", ".join(map(repr, expression.superscript_arguments))}"
                )
            else:
                superscript = (
                    f"^{{{', '.join(map(repr, expression.superscript_arguments))}}}"
                )

            return f"{expression.function.name}{subscript}{superscript}({', '.join(map(repr, expression.functional_arguments))})"
        case Derivative():
            parts = []
            for variable, order in expression.variables:
                if order == 1:
                    parts.append(render(variable))
                else:
                    parts.append(f"{render(variable)}^{order}")
            return f"d/d{','.join(parts)}({render(expression.expression)})"
        case Integral():
            if expression.lower is None or expression.upper is None:
                return (
                    f"int({render(expression.expression)}) d{render(expression.variable)}"
                )
            return (
                f"int_[{render(expression.lower)}..{render(expression.upper)}]"
                + f"({render(expression.expression)}) d{render(expression.variable)}"
            )
        case Symbol():
            return expression.name
        case Equation():
            return " = ".join(map(render, expression.expressions))
        case InEquality():
            return f"{render(expression.expression1)} {expression.sign} {render(expression.expression2)}"
        case SystemOfEquations():
            rendered_equations = [render(eq) for eq in expression.equations]
            return "{ " + " ; ".join(rendered_equations) + " }"


def render_latex(
    expression: Union[Numerical, Equation, InEquality, SystemOfEquations],
    renderOptions: LaTeXRenderOptions = LaTeXRenderOptions(),
    paren_group=False,
    square_group=False,
    curly_group=False,
):
    def _render_or_fallback(term):
        rendered = render_latex(term, renderOptions)
        return rendered if rendered is not None else str(term)

    match expression:
        case int() | float():
            if expression == math.pi:
                return "\\pi"
            return to_trimmed_decimal_string(expression)
        case complex():
            return f"({expression.real} + {expression.imag}i)"
        case Power(base, exponent) if (
            isinstance(expression.exponent, int)
            or isinstance(expression.exponent, float)
        ) and exponent < 0 and renderOptions.negative_exponent_as_fraction:
            if renderOptions.fraction_as_inline:
                return apply_group(
                    f"1/{render_latex(power(base, -exponent), renderOptions, True)}",
                    paren_group,
                    square_group,
                    curly_group,
                )
            else:
                return apply_group(
                    f"\\frac{{1}}{{{render_latex(power(base, -exponent), renderOptions)}}}",
                    paren_group,
                    square_group,
                    curly_group,
                )
        case Power(value, Power(base, exponent)) if (
            (isinstance(exponent, int) or isinstance(exponent, float))
            and isinstance(base, (int, float))
            and exponent < 0
        ):
            # Root
            try:
                root = base ** (-exponent)
            except OverflowError:
                # Fallback to generic power rendering when root degree is too large.
                return apply_group(
                    f"{render_latex(value, renderOptions, True)}^{{({render_latex(base, renderOptions, True)})^{{{render_latex(-exponent, renderOptions, True)}}}}}",
                    paren_group and renderOptions.group_exponentiation,
                    square_group and renderOptions.group_exponentiation,
                    curly_group and renderOptions.group_exponentiation,
                )
            if root == 2:
                return f"\\sqrt{{{render_latex(value, renderOptions)}}}"
            else:
                return f"\\sqrt[{root}]{{{render_latex(value, renderOptions)}}}"

        case Power() if (
            isinstance(expression.exponent, int)
            or isinstance(expression.exponent, float)
            and renderOptions.compact_exponents
        ):
            return apply_group(
                f"{render_latex(expression.base, renderOptions, True)}^{render_latex(expression.exponent, renderOptions)}",
                paren_group and renderOptions.group_exponentiation,
                square_group and renderOptions.group_exponentiation,
                curly_group and renderOptions.group_exponentiation,
            )
        case Power():
            return apply_group(
                f"{render_latex(expression.base, renderOptions, True)}^{{{render_latex(expression.exponent, renderOptions)}}}",
                paren_group and renderOptions.group_exponentiation,
                square_group and renderOptions.group_exponentiation,
                curly_group and renderOptions.group_exponentiation,
            )
        case Product():
            positive_exponents = []
            negative_exponents = []
            for factor in expression.factors:
                match factor:
                    case Power(base, exponent) if (
                        isinstance(exponent, int) or isinstance(exponent, float)
                    ) and exponent < 0:
                        negative_exponents.append(power(base, -exponent))
                    case _:
                        positive_exponents.append(factor)
            if len(negative_exponents) > 0:
                if renderOptions.fraction_as_inline:
                    return apply_group(
                        f"{render_latex(product(positive_exponents), renderOptions, True)}/{render_latex(product(negative_exponents), renderOptions, True)}",
                        paren_group,
                        square_group,
                        curly_group,
                    )
                return apply_group(
                    f"\\frac{{{render_latex(product(positive_exponents), renderOptions)}}}{{{render_latex(product(negative_exponents), renderOptions)}}}",
                    paren_group,
                    square_group,
                    curly_group,
                )
            else:
                result = ""
                prev = None
                prev_rendered = None
                for i, factor in enumerate(expression.factors):
                    rendered_factor = render_latex(factor, renderOptions, True)

                    if i > 0:
                        can_use_implicit = (
                            not (
                                (
                                    rendered_factor[0].isnumeric()
                                    and (prev_rendered[-1].isnumeric())
                                )
                                or rendered_factor[0] == "-"
                            )
                        ) or renderOptions.product_separator != ""
                        if (
                            not can_use_implicit
                            and renderOptions.use_parentheses_for_literal_product
                        ) or renderOptions.always_use_product_parentheses:
                            result += "(" + rendered_factor + ")"
                        elif not can_use_implicit:
                            result += " \\cdot " + rendered_factor
                        else:
                            result += renderOptions.product_separator + rendered_factor
                    else:
                        result += rendered_factor
                    prev_rendered = rendered_factor
                    prev = factor
                return result
        case Sum():
            return _render_sum_with_signs(
                expression.terms,
                renderer=lambda term: _render_or_fallback(term),
                apply_group_fn=apply_group,
                paren_group=paren_group,
                square_group=square_group,
                curly_group=curly_group,
            )
        case FunctionCall():
            if len(expression.subscript_arguments) == 0:
                subscript = ""
            elif len(expression.subscript_arguments) == 1:
                subscript = f"_{", ".join(map(lambda term: render_latex(term, renderOptions), expression.subscript_arguments))}"
            else:
                subscript = f"_{{{', '.join(map(lambda term: render_latex(term, renderOptions), expression.subscript_arguments))}}}"

            if len(expression.superscript_arguments) == 0:
                superscript = ""
            elif len(expression.superscript_arguments) == 1:
                superscript = f"^{", ".join(map(lambda term: render_latex(term, renderOptions), expression.superscript_arguments))}"
            else:
                superscript = f"^{{{', '.join(map(lambda term: render_latex(term, renderOptions), expression.superscript_arguments))}}}"
            arguments = ", ".join(
                map(
                    lambda term: render_latex(term, renderOptions),
                    expression.functional_arguments,
                )
            )
            if (
                len(expression.functional_arguments) == 1
                and not renderOptions.group_on_one_argument_function
            ):
                output = (
                    f"{expression.function.name}{subscript}{superscript} {arguments}"
                )
            elif renderOptions.parentheses_function_call:
                output = (
                    f"{expression.function.name}{subscript}{superscript}({arguments})"
                )
            else:
                output = (
                    f"{expression.function.name}{subscript}{superscript}{{{arguments}}}"
                )
            if renderOptions.backslash_function_call:
                output = "\\" + output
            return output
        case Derivative():
            total_order = sum(order for _, order in expression.variables)
            den = " ".join(
                [
                    (
                        f"d{render_latex(variable, renderOptions)}"
                        if order == 1
                        else f"d{render_latex(variable, renderOptions)}^{{{order}}}"
                    )
                    for variable, order in expression.variables
                ]
            )
            if total_order == 1:
                num = "d"
            else:
                num = f"d^{{{total_order}}}"
            body = render_latex(expression.expression, renderOptions)
            return apply_group(
                f"\\frac{{{num}}}{{{den}}}{body}",
                paren_group,
                square_group,
                curly_group,
            )
        case Integral():
            integrand = render_latex(expression.expression, renderOptions)
            variable = render_latex(expression.variable, renderOptions)
            if expression.lower is None or expression.upper is None:
                output = f"\\int {integrand} \\, d{variable}"
            else:
                lower = render_latex(expression.lower, renderOptions)
                upper = render_latex(expression.upper, renderOptions)
                output = f"\\int_{{{lower}}}^{{{upper}}} {integrand} \\, d{variable}"
            return apply_group(output, paren_group, square_group, curly_group)
        case Symbol():
            return expression.name
        case Equation():
            return " = ".join(
                map(
                    lambda term: render_latex(term, renderOptions),
                    expression.expressions,
                )
            )
        case InEquality():
            return f"{render_latex(expression.expression1, renderOptions)} {expression.sign} {render_latex(expression.expression2, renderOptions)}"
        case SystemOfEquations():
            rows = [render_latex(eq, renderOptions) for eq in expression.equations]
            return "\\left\\{\\begin{array}{l}" + " \\\\ ".join(rows) + "\\end{array}\\right."
        case _:
            return apply_group(
                str(expression),
                paren_group,
                square_group,
                curly_group,
            )


def render_type(expression: Numerical, indent=0):
    indent_str = ""  # 2 * indent * " "
    match expression:
        case int() | float():
            result = str(expression)
        case Power():
            result = f"Power(\n{render_type(expression.base, indent + 1)},\n{render_type(expression.exponent, indent + 1)}\n{indent_str})"
        case Product():
            result = f"Product([\n{",\n".join([render_type(factor, indent + 1) for factor in expression.factors])}\n{indent_str}])"
        case Sum():
            result = f"Sum([\n{",\n".join([render_type(term, indent + 1) for term in expression.terms])}\n{indent_str}])"
        case FunctionCall():
            result = f"FunctionCall([\n{",\n".join([render_type(term, indent + 1) for term in expression.functional_arguments])}\n],\n[\n{",\n".join([render_type(term, indent + 1) for term in expression.subscript_arguments])}\n],\n[\n{",\n".join([render_type(term, indent + 1) for term in expression.superscript_arguments])}\n{indent_str}])"
        case Derivative():
            parts = ", ".join([f"({render_type(v)}, {o})" for v, o in expression.variables])
            result = (
                f"Derivative({render_type(expression.expression, indent + 1)}, [{parts}])"
            )
        case Integral():
            lower = (
                render_type(expression.lower, indent + 1)
                if expression.lower is not None
                else "None"
            )
            upper = (
                render_type(expression.upper, indent + 1)
                if expression.upper is not None
                else "None"
            )
            result = (
                f"Integral({render_type(expression.expression, indent + 1)}, "
                + f"{render_type(expression.variable, indent + 1)}, {lower}, {upper})"
            )
        case Symbol():
            result = f'Symbol("{expression.name}")'
        case complex():
            result = f"complex({expression.real}, {expression.imag})"
        case _:
            result = "Unknown"

    return (indent_str + result).replace("\n", "")


if __name__ == "__main__":
    # expression = sum([power(2, 3), product([2, power(Symbol("x"), 2)])])
    # expression = (expression * 2) / 3
    # print(render_latex(expression))

    # expression = power(2, fraction(1, 3))
    # print(render_latex(expression))

    # 1. Simple sum and product
    expression1 = Sum([Power(-18, -1.9), 4, Product([-47, 0])])
    print(render(expression1))
    print(render_latex(expression1))
    print()
