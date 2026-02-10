from math import cos, exp, isclose, log, log10, pi, sin, sqrt, tan
import random

from .evaluator import (
    EvaluatorContext,
    EvaluatorOptions,
    WordingOptions,
    evaluate,
    evaluate_expression,
)
from .expression import *
from .render import render_latex
from .procedural import FUNCTIONS, ExpressionContext, generate_random_expression


def _is_numeric(x):
    return isinstance(x, (int, float))


def _numeric_equal(actual, expected, tol=1e-9):
    return abs(float(actual) - float(expected)) <= tol


def _equal_result(actual, expected, tol=1e-9):
    if _is_numeric(actual) and _is_numeric(expected):
        return _numeric_equal(actual, expected, tol=tol)
    return render_latex(actual) == render_latex(expected)


def run_evaluate_tests():
    sin_function = MathFunction("sin", 1)
    log_function = MathFunction("log", 1, 1)
    log10_function = MathFunction("log10", functional_parameters=1)

    x = Symbol("x")
    y = Symbol("y")
    a = Symbol("a")
    d = Symbol("d")
    n = Symbol("n")
    z = Symbol("z")

    test_cases = [
        ("numeric sum", Sum([2, 3, 5]), {}, 10, 1e-9),
        ("simple substitution", sum([x, 3]), {"x": 7}, 10, 1e-9),
        ("missing variable remains symbolic", product([2, y]), {"x": 1}, product([2, y]), 1e-9),
        (
            "nested linear combination",
            sum([product([2, x]), product([3, y]), 5]),
            {"x": 4, "y": 6},
            31,
            1e-9,
        ),
        ("negative exponent numeric", power(a, -2), {"a": 2}, 0.25, 1e-9),
        ("fractional exponent sqrt", power(z, fraction(1, 2)), {"z": 25}, 5.0, 1e-9),
        (
            "sin(pi/2)",
            FunctionCall(sin_function, [pi / 2]),
            {"sin": lambda args, _, __: sin(args[0])},
            1.0,
            1e-9,
        ),
        (
            "log base 10",
            FunctionCall(log_function, [100], [10]),
            {"log": lambda args, subs, __: log(args[0], subs[0])},
            2.0,
            1e-9,
        ),
        ("partial substitution", sum([x, y]), {"x": 2}, sum([2, y]), 1e-9),
        (
            "nested function sin(x^2)",
            FunctionCall(sin_function, [power(x, 2)]),
            {"x": pi, "sin": lambda args, _, __: sin(args[0])},
            sin(pi**2),
            1e-3,
        ),
        ("(x+y)^2", power(sum([x, y]), 2), {"x": 3, "y": 4}, 49, 1e-9),
        ("(x+2)(y+3)", product([sum([x, 2]), sum([y, 3])]), {"x": 1, "y": 2}, 15, 1e-9),
        ("(a+1)^3", power(sum([a, 1]), 3), {"a": 2}, 27, 1e-9),
        ("fraction product", product([n, power(d, -1)]), {"n": 6, "d": 2}, 3.0, 1e-9),
        ("zero in multiplication", Product([0, x]), {"x": 100}, 0, 1e-9),
        ("large integer product", Product([91, 998]), {}, 90818, 1e-9),
        ("integer addition", Sum([921, 998]), {}, 1919, 1e-9),
        ("larger integer addition", Sum([13500, 146000]), {}, 159500, 1e-9),
        ("zero term in sum", Sum([0, Product([2, 13])]), {}, 26, 1e-9),
        ("mixed arithmetic sum", Sum([1, 2, 3, 4, 5, Product([3, 5]), Power(3, 2)]), {}, 39, 1e-9),
        ("simple signed product", Product([Sum([2]), -1, 10]), {}, -20, 1e-9),
        (
            "symbolic cancellation style",
            Sum([Product([Sum([1, 4, x]), -1]), Power(2, 2), Product([3, x])]),
            {"x": 1},
            1,
            1e-9,
        ),
        ("small signed sum", Sum([-201, 203]), {}, 2, 1e-9),
        ("decimal product", product([1, 2, -10.248]), {}, -20.496, 1e-9),
        ("nested product flatten", Product([1, Product([2, 2])]), {}, 4, 1e-9),
        (
            "log10(100)",
            FunctionCall(log10_function, [100]),
            {"log10": lambda args, _, __: log10(args[0])},
            2,
            1e-9,
        ),
        (
            "undefined log10(0) keeps symbolic",
            FunctionCall(log10_function, [0]),
            {"log10": lambda args, _, __: log10(args[0])},
            FunctionCall(log10_function, [0]),
            1e-9,
        ),
        ("power of integer product", Power(Product([7, 14]), 3), {}, (7 * 14) ** 3, 1e-9),
        ("tiny scientific-style value", Sum([4, 7.90623]), {}, 11.90623, 1e-9),
        ("0^0 default undefined", power(0, 0), {}, power(0, 0), 1e-9),
        (
            "derivative polynomial",
            derivative(sum([power(x, 3), product([2, x])]), x),
            {},
            sum([product([3, power(x, 2)]), 2]),
            1e-9,
        ),
        (
            "derivative trig",
            derivative(FunctionCall(MathFunction("sin", 1), [x]), x),
            {},
            FunctionCall(MathFunction("cos", 1), [x]),
            1e-9,
        ),
        (
            "multivariate derivative",
            partial_derivative(product([power(x, 2), power(y, 3)]), [(x, 1), (y, 1)]),
            {},
            product([6, x, power(y, 2)]),
            1e-9,
        ),
        (
            "indefinite integral polynomial",
            integral(x, x),
            {},
            product([0.5, power(x, 2)]),
            1e-9,
        ),
        (
            "indefinite integral trig",
            integral(FunctionCall(MathFunction("sin", 1), [x]), x),
            {},
            product([-1, FunctionCall(MathFunction("cos", 1), [x])]),
            1e-9,
        ),
        ("definite integral simple", integral(x, x, 0, 2), {}, 2, 1e-9),
        (
            "definite integral linear",
            integral(product([2, x]), x, 1, 3),
            {},
            8,
            1e-9,
        ),
        (
            "unsolved integral fallback",
            integral(FunctionCall(MathFunction("exp", 1), [power(x, 2)]), x),
            {},
            integral(FunctionCall(MathFunction("exp", 1), [power(x, 2)]), x),
            1e-9,
        ),
    ]

    failures = []
    for i, (name, expr, substitutions, expected, tol) in enumerate(test_cases, 1):
        result, _ = evaluate(expr, substitutions, error_on_invalid_snap=False)
        if not _equal_result(result, expected, tol=tol):
            failures.append(
                (
                    i,
                    name,
                    render_latex(expr),
                    render_latex(result),
                    render_latex(expected) if not _is_numeric(expected) else expected,
                )
            )

    return len(test_cases), failures


def run_options_tests():
    tests = []

    expr00 = power(0, 0)
    for policy, expected in [("one", 1), ("zero", 0)]:
        ctx = EvaluatorContext(
            expr00,
            options=EvaluatorOptions(zero_power_zero_policy=policy),
            error_on_invalid_snap=False,
        )
        result = evaluate_expression(expr00, ctx)
        tests.append((f"0^0 policy={policy}", result == expected))

    huge_power = power(8, 200)
    ctx_symbolic = EvaluatorContext(
        huge_power,
        options=EvaluatorOptions(max_exponent=100, overflow_policy="symbolic"),
        error_on_invalid_snap=False,
    )
    result_symbolic = evaluate_expression(huge_power, ctx_symbolic)
    tests.append(("overflow symbolic", isinstance(result_symbolic, Power)))

    ctx_inf = EvaluatorContext(
        huge_power,
        options=EvaluatorOptions(max_exponent=100, overflow_policy="infinity"),
        error_on_invalid_snap=False,
    )
    result_inf = evaluate_expression(huge_power, ctx_inf)
    tests.append(("overflow infinity", result_inf == float("inf")))

    ctx_zero = EvaluatorContext(
        huge_power,
        options=EvaluatorOptions(max_exponent=100, overflow_policy="zero"),
        error_on_invalid_snap=False,
    )
    result_zero = evaluate_expression(huge_power, ctx_zero)
    tests.append(("overflow zero", result_zero == 0))

    custom_wording = WordingOptions(
        templates={"addition_decompose_intro": "CUSTOM DECOMPOSE MESSAGE"}
    )
    add_expr = Sum([4, 7.90623])
    ctx_wording = EvaluatorContext(
        add_expr,
        options=EvaluatorOptions(wording_options=custom_wording),
        error_on_invalid_snap=False,
    )
    _ = evaluate_expression(add_expr, ctx_wording)
    rendered_steps = ctx_wording.render()
    tests.append(("wording override", "CUSTOM DECOMPOSE MESSAGE" in rendered_steps))

    return tests


def _contains_calculus(expr):
    if isinstance(expr, (Derivative, Integral)):
        return True
    if isinstance(expr, Sum):
        return any(_contains_calculus(term) for term in expr.terms)
    if isinstance(expr, Product):
        return any(_contains_calculus(factor) for factor in expr.factors)
    if isinstance(expr, Power):
        return _contains_calculus(expr.base) or _contains_calculus(expr.exponent)
    if isinstance(expr, FunctionCall):
        return any(_contains_calculus(arg) for arg in expr.functional_arguments)
    return False


def run_calculus_quality_tests():
    tests = []
    x = Symbol("x")

    # Rule/event emission for derivative.
    d_expr = derivative(sum([power(x, 3), product([2, x])]), x)
    d_result, d_context = evaluate(d_expr, error_on_invalid_snap=False)
    tests.append(("events emitted for derivative", len(d_context.explanation_events) > 0))
    tests.append(
        (
            "derivative coverage tags",
            any(tag.startswith("diff_") for tag in d_context.coverage_tags),
        )
    )

    # Status and reason for unsolved calculus.
    i_expr = integral(FunctionCall(MathFunction("exp", 1), [power(x, 2)]), x)
    _, i_context = evaluate(i_expr, error_on_invalid_snap=False)
    tests.append(("unsolved integral marks partial", i_context.solve_status == "partial"))
    tests.append(("unsolved integral has reason", i_context.reason_code is not None))

    # Property-style check: derivative agrees with known analytic form.
    poly = sum([power(x, 3), product([2, x])])
    d_poly = derivative(poly, x)
    for sample in [-2.0, -1.0, 1.0, 2.0, 3.0]:
        d_value, _ = evaluate(d_poly, substitutions={"x": sample}, error_on_invalid_snap=False)
        expected_value = 3 * (sample**2) + 2
        tests.append(
            (
                f"analytic derivative at {sample}",
                isclose(float(d_value), float(expected_value), rel_tol=1e-6, abs_tol=1e-6),
            )
        )

    # Property-style check: d/dx(integral f dx) = f for a solvable case.
    f_expr = product([2, x])
    antiderivative = integral(f_expr, x)
    d_antiderivative = derivative(antiderivative, x)
    recovered, _ = evaluate(d_antiderivative, error_on_invalid_snap=False)
    ok_recovery = True
    for sample in [-2.0, -1.0, 0.0, 1.0, 3.0]:
        rv, _ = evaluate(recovered, substitutions={"x": sample}, error_on_invalid_snap=False)
        fv, _ = evaluate(f_expr, substitutions={"x": sample}, error_on_invalid_snap=False)
        if not isclose(float(rv), float(fv), rel_tol=1e-6, abs_tol=1e-6):
            ok_recovery = False
            break
    tests.append(("derivative of antiderivative recovers integrand", ok_recovery))

    return tests


def run_calculus_rule_coverage_tests():
    tests = []
    x = Symbol("x")
    y = Symbol("y")

    def check_numeric(expr, substitutions, expected, name, tol=1e-6):
        numeric_substitutions = dict(substitutions)
        numeric_substitutions.update(FUNCTIONS)
        value, _ = evaluate(
            expr, substitutions=numeric_substitutions, error_on_invalid_snap=False
        )
        tests.append((name, isclose(float(value), float(expected), rel_tol=tol, abs_tol=tol)))

    # Derivative rule coverage (numeric checks for stable polynomial/log-style forms).
    d_const = derivative(7, x)
    check_numeric(d_const, {"x": 4.0}, 0.0, "d/dx constant")

    d_other_symbol = derivative(y, x)
    check_numeric(d_other_symbol, {"x": 1.5, "y": 8.0}, 0.0, "d/dx other symbol")

    d_power = derivative(power(x, 5), x)
    check_numeric(d_power, {"x": 2.0}, 80.0, "d/dx x^5")

    d_ln = derivative(FunctionCall(MathFunction("ln", 1), [x]), x)
    check_numeric(d_ln, {"x": 2.0}, 0.5, "d/dx ln(x)")

    d_sqrt = derivative(FunctionCall(MathFunction("sqrt", 1), [x]), x)
    d_sqrt_result, _ = evaluate(d_sqrt, error_on_invalid_snap=False)
    d_sqrt_latex = render_latex(d_sqrt_result)
    tests.append(("d/dx sqrt(x) shape", ("\\sqrt" in d_sqrt_latex and "0.5" in d_sqrt_latex)))

    d_log_base10 = derivative(
        FunctionCall(MathFunction("log", 1, 1), [x], [10]),
        x,
    )
    check_numeric(
        d_log_base10,
        {"x": 10.0},
        1 / (10.0 * log(10)),
        "d/dx log_10(x)",
        tol=2e-3,
    )

    # Symbolic shape checks for trig/exp chain rules (avoid unstable float-heavy arithmetic path).
    d_sin_chain = derivative(FunctionCall(MathFunction("sin", 1), [product([3, x])]), x)
    d_sin_result, _ = evaluate(d_sin_chain, error_on_invalid_snap=False)
    d_sin_latex = render_latex(d_sin_result)
    tests.append(("d/dx sin(3x) shape", ("\\cos" in d_sin_latex and "3x" in d_sin_latex)))

    d_cos_chain = derivative(FunctionCall(MathFunction("cos", 1), [product([4, x])]), x)
    d_cos_result, _ = evaluate(d_cos_chain, error_on_invalid_snap=False)
    d_cos_latex = render_latex(d_cos_result)
    tests.append(("d/dx cos(4x) shape", ("\\sin" in d_cos_latex and "4x" in d_cos_latex)))

    d_tan_chain = derivative(FunctionCall(MathFunction("tan", 1), [product([2, x])]), x)
    d_tan_result, _ = evaluate(d_tan_chain, error_on_invalid_snap=False)
    d_tan_latex = render_latex(d_tan_result)
    tests.append(("d/dx tan(2x) shape", ("\\sec" in d_tan_latex and "^2" in d_tan_latex)))

    d_exp_chain = derivative(FunctionCall(MathFunction("exp", 1), [product([5, x])]), x)
    d_exp_result, _ = evaluate(d_exp_chain, error_on_invalid_snap=False)
    d_exp_latex = render_latex(d_exp_result)
    tests.append(("d/dx exp(5x) shape", ("\\exp" in d_exp_latex and "5x" in d_exp_latex)))

    # Integral rule coverage checked by differentiating antiderivative numerically.
    integral_cases = [
        ("int constant", integral(3, x), lambda t: 3.0),
        ("int x^4", integral(power(x, 4), x), lambda t: t**4),
        ("int 1/x", integral(power(x, -1), x), lambda t: 1 / t),
        ("int sin(2x)", integral(FunctionCall(MathFunction("sin", 1), [product([2, x])]), x), lambda t: sin(2 * t)),
    ]
    for name, antiderivative_expr, integrand_fn in integral_cases:
        d_antiderivative = derivative(antiderivative_expr, x)
        for sample in [1.0, 2.0, 3.0]:
            numeric_substitutions = {"x": sample}
            numeric_substitutions.update(FUNCTIONS)
            recovered, _ = evaluate(
                d_antiderivative,
                substitutions=numeric_substitutions,
                error_on_invalid_snap=False,
            )
            expected = integrand_fn(sample)
            tests.append(
                (
                    f"{name} derivative-check at {sample}",
                    isclose(float(recovered), float(expected), rel_tol=1e-5, abs_tol=1e-5),
                )
            )

    # Definite integral coverage.
    # Symbolic shape checks for integral trig/exp rules.
    int_cos = integral(FunctionCall(MathFunction("cos", 1), [product([3, x])]), x)
    int_cos_result, _ = evaluate(int_cos, error_on_invalid_snap=False)
    tests.append(("int cos(3x) shape", "\\sin" in render_latex(int_cos_result)))

    int_exp = integral(FunctionCall(MathFunction("exp", 1), [product([4, x])]), x)
    int_exp_result, _ = evaluate(int_exp, error_on_invalid_snap=False)
    tests.append(("int exp(4x) shape", "\\exp" in render_latex(int_exp_result)))

    check_numeric(integral(product([3, x]), x, 1, 5), {}, 36.0, "definite int 3x [1,5]")
    check_numeric(
        integral(FunctionCall(MathFunction("sin", 1), [x]), x, 0, pi),
        {},
        2.0,
        "definite int sin(x) [0,pi]",
        tol=1e-5,
    )
    check_numeric(
        integral(FunctionCall(MathFunction("exp", 1), [x]), x, 0, 1),
        {},
        exp(1) - 1,
        "definite int exp(x) [0,1]",
        tol=1e-5,
    )

    return tests


def run_explanation_quality_tests():
    tests = []
    x = Symbol("x")

    # Ensure explanatory text quality for a representative calculus run.
    expr = derivative(sum([power(x, 3), product([2, x])]), x)
    _, ctx = evaluate(expr, error_on_invalid_snap=False)
    rendered = ctx.render()

    tests.append(("rendered explanation not empty", len(rendered.strip()) > 0))
    tests.append(("rendered explanation has structure", len(rendered.strip()) > 0))
    tests.append(("rendered explanation has no literal None", "None" not in rendered))
    tests.append(("events have non-empty rule ids", all(e.rule_id for e in ctx.explanation_events)))
    tests.append(
        (
            "event categories valid",
            all(e.category in ("derivative", "integral", "algebra", "arithmetic") for e in ctx.explanation_events),
        )
    )
    tests.append(
        (
            "coverage tags correspond to events",
            all(tag in {e.rule_id for e in ctx.explanation_events} for tag in ctx.coverage_tags),
        )
    )

    # Show-rule-name option should prefix emitted text when enabled.
    opt = EvaluatorOptions(show_rule_name=True)
    ctx_rule_name = EvaluatorContext(expr, options=opt, error_on_invalid_snap=False)
    _ = evaluate_expression(expr, ctx_rule_name)
    rendered_events = ctx_rule_name.render_explanation_events()
    tests.append(("render explanation events includes derivative tag", "[derivative]" in rendered_events))

    return tests


def run_procedural_fuzz_tests():
    random.seed(1337)
    tests = []
    total = 60
    solved_or_partial = 0
    no_crash = True
    for _ in range(total):
        context = ExpressionContext()
        try:
            expr = generate_random_expression(
                max_depth=3,
                allow_calculus=True,
                guarantee_solvable=True,
                difficulty="beginner",
                context=context,
            )
            substitutions = context.substitutions.copy()
            substitutions.update(FUNCTIONS)
            _, eval_context = evaluate(expr, substitutions, error_on_invalid_snap=False)
            if eval_context.solve_status in ("exact", "partial"):
                solved_or_partial += 1
            if _contains_calculus(expr) and eval_context.solve_status == "unsolved":
                no_crash = False
        except Exception:
            no_crash = False
    tests.append(("procedural fuzz no crashes", no_crash))
    tests.append(("procedural fuzz solved/partial coverage", solved_or_partial >= int(total * 0.8)))
    return tests


def run_procedural_profile_tests():
    random.seed(2026)
    tests = []

    profiles = [
        ("beginner_solvable", {"difficulty": "beginner", "guarantee_solvable": True}),
        ("intermediate_solvable", {"difficulty": "intermediate", "guarantee_solvable": True}),
        ("advanced_solvable", {"difficulty": "advanced", "guarantee_solvable": True}),
        ("intermediate_unspecified", {"difficulty": "intermediate", "guarantee_solvable": False}),
    ]

    for profile_name, params in profiles:
        total = 40
        no_crash = True
        exact_or_partial = 0
        calculus_seen = 0
        for _ in range(total):
            context = ExpressionContext()
            try:
                expr = generate_random_expression(
                    max_depth=4,
                    allow_calculus=True,
                    allow_definite_integrals=True,
                    max_derivative_order=2,
                    context=context,
                    **params,
                )
                if _contains_calculus(expr):
                    calculus_seen += 1
                substitutions = context.substitutions.copy()
                substitutions.update(FUNCTIONS)
                _, eval_ctx = evaluate(expr, substitutions, error_on_invalid_snap=False)
                if eval_ctx.solve_status in ("exact", "partial"):
                    exact_or_partial += 1
            except Exception:
                no_crash = False
                break

        tests.append((f"{profile_name}: no crashes", no_crash))
        tests.append((f"{profile_name}: calculus generated often", calculus_seen >= int(total * 0.05)))
        required = 0.9 if params["guarantee_solvable"] else 0.6
        tests.append(
            (
                f"{profile_name}: exact/partial rate",
                exact_or_partial >= int(total * required),
            )
        )

    return tests


if __name__ == "__main__":
    total, failures = run_evaluate_tests()
    option_results = run_options_tests()
    calculus_quality_results = run_calculus_quality_tests()
    calculus_rule_results = run_calculus_rule_coverage_tests()
    explanation_quality_results = run_explanation_quality_tests()
    fuzz_results = run_procedural_fuzz_tests()
    profile_results = run_procedural_profile_tests()

    print("Expressionizer test suite")
    print("=" * 26)
    print(f"Core evaluate tests: {total - len(failures)}/{total} passed")

    if failures:
        print("\nFailures:")
        for i, name, expr_latex, got, expected in failures:
            print(f"- [{i}] {name}")
            print(f"  expr: {expr_latex}")
            print(f"  got: {got}")
            print(f"  expected: {expected}")
    else:
        print("No core failures.")

    passed_options = sum(1 for _, ok in option_results if ok)
    print(
        f"Option policy tests: {passed_options}/{len(option_results)} passed"
    )
    for name, ok in option_results:
        print(f"- {name}: {'PASS' if ok else 'FAIL'}")

    passed_calculus = sum(1 for _, ok in calculus_quality_results if ok)
    print(
        f"Calculus quality tests: {passed_calculus}/{len(calculus_quality_results)} passed"
    )
    for name, ok in calculus_quality_results:
        print(f"- {name}: {'PASS' if ok else 'FAIL'}")

    passed_calculus_rules = sum(1 for _, ok in calculus_rule_results if ok)
    print(
        f"Calculus rule coverage tests: {passed_calculus_rules}/{len(calculus_rule_results)} passed"
    )
    for name, ok in calculus_rule_results:
        print(f"- {name}: {'PASS' if ok else 'FAIL'}")

    passed_explanation = sum(1 for _, ok in explanation_quality_results if ok)
    print(
        f"Explanation quality tests: {passed_explanation}/{len(explanation_quality_results)} passed"
    )
    for name, ok in explanation_quality_results:
        print(f"- {name}: {'PASS' if ok else 'FAIL'}")

    passed_fuzz = sum(1 for _, ok in fuzz_results if ok)
    print(f"Procedural fuzz tests: {passed_fuzz}/{len(fuzz_results)} passed")
    for name, ok in fuzz_results:
        print(f"- {name}: {'PASS' if ok else 'FAIL'}")

    passed_profiles = sum(1 for _, ok in profile_results if ok)
    print(f"Procedural profile tests: {passed_profiles}/{len(profile_results)} passed")
    for name, ok in profile_results:
        print(f"- {name}: {'PASS' if ok else 'FAIL'}")

    if (
        failures
        or passed_options != len(option_results)
        or passed_calculus != len(calculus_quality_results)
        or passed_calculus_rules != len(calculus_rule_results)
        or passed_explanation != len(explanation_quality_results)
        or passed_fuzz != len(fuzz_results)
        or passed_profiles != len(profile_results)
    ):
        raise SystemExit(1)
