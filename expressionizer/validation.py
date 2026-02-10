import math
from typing import Any

from .evaluator import contains, replace_sub
from .expression import Derivative, FunctionCall, Integral, Power, Product, Sum, Symbol
from .render import render_latex

try:
    import sympy as sp
except Exception:
    sp = None


def _sympy_num(value: int | float):
    if isinstance(value, int):
        return sp.Integer(value)
    if isinstance(value, float):
        if math.isnan(value):
            return sp.nan
        if math.isinf(value):
            return sp.oo if value > 0 else -sp.oo
        return sp.Float(repr(value))
    raise TypeError(f"Unsupported numeric type: {type(value)}")


def _map_function(name: str):
    mapping = {
        "sin": sp.sin,
        "cos": sp.cos,
        "tan": sp.tan,
        "asin": sp.asin,
        "acos": sp.acos,
        "atan": sp.atan,
        "atan2": sp.atan2,
        "csc": sp.csc,
        "sec": sp.sec,
        "cot": sp.cot,
        "sinh": sp.sinh,
        "cosh": sp.cosh,
        "tanh": sp.tanh,
        "asinh": sp.asinh,
        "acosh": sp.acosh,
        "atanh": sp.atanh,
        "ln": sp.log,
        "log10": lambda x: sp.log(x, 10),
        "log2": lambda x: sp.log(x, 2),
        "log1p": lambda x: sp.log(1 + x),
        "exp": sp.exp,
        "expm1": lambda x: sp.exp(x) - 1,
        "pow": sp.Pow,
        "sqrt": sp.sqrt,
        "ceil": sp.ceiling,
        "floor": sp.floor,
        "trunc": lambda x: sp.Integer(x) if getattr(x, "is_integer", False) else sp.floor(x),
        "abs": sp.Abs,
        "factorial": sp.factorial,
        "gcd": sp.gcd,
        "lcm": sp.lcm,
        "perm": lambda n, k: sp.factorial(n) / sp.factorial(n - k),
        "comb": sp.binomial,
        "gamma": sp.gamma,
        "lgamma": sp.loggamma,
        "erf": sp.erf,
        "erfc": sp.erfc,
    }
    return mapping.get(name)


def to_sympy(expr: Any):
    if sp is None:
        raise RuntimeError("SymPy is not available")

    if isinstance(expr, (int, float)):
        return _sympy_num(expr)
    if isinstance(expr, Symbol):
        return sp.Symbol(expr.name)
    if isinstance(expr, Power):
        return sp.Pow(to_sympy(expr.base), to_sympy(expr.exponent))
    if isinstance(expr, Product):
        factors = [to_sympy(f) for f in expr.factors]
        if not factors:
            return sp.Integer(1)
        return sp.Mul(*factors)
    if isinstance(expr, Sum):
        terms = [to_sympy(t) for t in expr.terms]
        if not terms:
            return sp.Integer(0)
        return sp.Add(*terms)
    if isinstance(expr, FunctionCall):
        fn_name = expr.function.name
        args = [to_sympy(a) for a in expr.functional_arguments]
        sub_args = [to_sympy(a) for a in expr.subscript_arguments]
        if fn_name == "log":
            if len(args) != 1:
                raise ValueError("log conversion expects one functional argument")
            if len(sub_args) == 1:
                return sp.log(args[0], sub_args[0])
            return sp.log(args[0])
        if fn_name == "root":
            if len(args) != 1:
                raise ValueError("root conversion expects one functional argument")
            degree = sub_args[0] if len(sub_args) == 1 else sp.Integer(2)
            return sp.Pow(args[0], sp.Integer(1) / degree)
        fn = _map_function(fn_name)
        if fn is None:
            return sp.Function(fn_name)(*args)
        return fn(*args)
    if isinstance(expr, Derivative):
        out = to_sympy(expr.expression)
        for variable, order in expr.variables:
            out = sp.diff(out, sp.Symbol(variable.name), order)
        return out
    if isinstance(expr, Integral):
        inner = to_sympy(expr.expression)
        symbol = sp.Symbol(expr.variable.name)
        if expr.lower is not None and expr.upper is not None:
            return sp.integrate(inner, (symbol, to_sympy(expr.lower), to_sympy(expr.upper)))
        return sp.integrate(inner, symbol)

    raise TypeError(f"Unsupported expression type for sympy conversion: {type(expr)}")


def _build_subs_map(substitutions: dict[str, Any] | None) -> dict[Any, Any]:
    if sp is None or not substitutions:
        return {}
    result = {}
    for name, value in substitutions.items():
        if not isinstance(name, str):
            continue
        if isinstance(value, (int, float)):
            result[sp.Symbol(name)] = _sympy_num(value)
    return result


def _complexity_info(expr: Any, max_nodes: int = 500) -> dict[str, Any]:
    visited: set[int] = set()
    stack: list[Any] = [expr]
    nodes = 0

    while stack:
        current = stack.pop()
        if isinstance(current, (int, float, str)) or current is None:
            continue
        if isinstance(current, tuple):
            stack.extend(list(current))
            continue
        if isinstance(current, list):
            stack.extend(current)
            continue

        current_id = id(current)
        if current_id in visited:
            return {"ok": False, "reason": "cyclic_expression", "nodes": nodes}
        visited.add(current_id)
        nodes += 1
        if nodes > max_nodes:
            return {"ok": False, "reason": "expression_too_large", "nodes": nodes}

        if isinstance(current, Power):
            stack.append(current.base)
            stack.append(current.exponent)
        elif isinstance(current, Product):
            stack.extend(current.factors)
        elif isinstance(current, Sum):
            stack.extend(current.terms)
        elif isinstance(current, FunctionCall):
            stack.extend(current.functional_arguments)
            stack.extend(current.subscript_arguments)
            stack.extend(current.superscript_arguments)
        elif isinstance(current, Derivative):
            stack.append(current.expression)
            for variable, order in current.variables:
                stack.append(variable)
                stack.append(order)
        elif isinstance(current, Integral):
            stack.append(current.expression)
            stack.append(current.variable)
            if current.lower is not None:
                stack.append(current.lower)
            if current.upper is not None:
                stack.append(current.upper)
        elif isinstance(current, Symbol):
            continue
        else:
            return {"ok": False, "reason": "unsupported_expression_type", "nodes": nodes}

    return {"ok": True, "nodes": nodes}


def compare_with_sympy(
    original_expr: Any,
    evaluated_result: Any,
    substitutions: dict[str, Any] | None = None,
    tolerance: float = 1e-8,
    max_expr_chars: int = 220,
) -> dict[str, Any]:
    if sp is None:
        return {"status": "skipped", "reason": "sympy_unavailable"}

    try:
        original_complexity = _complexity_info(original_expr)
        if not original_complexity.get("ok", False):
            return {
                "status": "inconclusive",
                "reason": original_complexity.get("reason", "complexity_guard"),
                "nodes": original_complexity.get("nodes"),
                "target": "original_expr",
            }
        result_complexity = _complexity_info(evaluated_result)
        if not result_complexity.get("ok", False):
            return {
                "status": "inconclusive",
                "reason": result_complexity.get("reason", "complexity_guard"),
                "nodes": result_complexity.get("nodes"),
                "target": "evaluated_result",
            }

        original_sym = to_sympy(original_expr)
        result_sym = to_sympy(evaluated_result)
        if len(str(original_sym)) > max_expr_chars or len(str(result_sym)) > max_expr_chars:
            return {
                "status": "inconclusive",
                "reason": "expression_too_complex_for_sympy",
            }
        subs_map = _build_subs_map(substitutions)

        lhs = sp.simplify(original_sym.subs(subs_map))
        rhs = sp.simplify(result_sym.subs(subs_map))
        diff = sp.simplify(lhs - rhs)
        if diff == 0:
            return {"status": "equivalent", "kind": "symbolic", "difference": "0"}

        lhs_num = sp.N(lhs)
        rhs_num = sp.N(rhs)
        if hasattr(lhs_num, "equals") and lhs_num.equals(rhs_num):
            return {"status": "equivalent", "kind": "numeric_symbolic_equals"}
        if str(lhs_num) == str(rhs_num):
            return {"status": "equivalent", "kind": "numeric_text_equal"}
        if lhs_num.is_real and rhs_num.is_real:
            try:
                lhs_float = float(lhs_num)
                rhs_float = float(rhs_num)
                abs_diff = abs(lhs_float - rhs_float)
                rel_diff = abs_diff / max(1.0, abs(lhs_float), abs(rhs_float))
            except (OverflowError, ValueError):
                abs_diff_expr = sp.N(sp.Abs(lhs_num - rhs_num))
                rel_expr = sp.N(
                    abs_diff_expr / sp.Max(sp.Integer(1), sp.Abs(lhs_num), sp.Abs(rhs_num))
                )
                try:
                    abs_diff = float(abs_diff_expr)
                except (OverflowError, ValueError, TypeError):
                    abs_diff = None
                try:
                    rel_diff = float(rel_expr)
                except (OverflowError, ValueError, TypeError):
                    rel_diff = None
            if (
                isinstance(abs_diff, float)
                and isinstance(rel_diff, float)
                and (math.isfinite(abs_diff) and math.isfinite(rel_diff))
                and (abs_diff <= tolerance or rel_diff <= tolerance)
            ):
                return {
                    "status": "equivalent",
                    "kind": "numeric",
                    "abs_diff": abs_diff,
                    "rel_diff": rel_diff,
                }
            if (
                isinstance(rel_diff, float)
                and math.isfinite(rel_diff)
                and rel_diff <= tolerance
            ):
                return {
                    "status": "equivalent",
                    "kind": "numeric",
                    "abs_diff": abs_diff,
                    "rel_diff": rel_diff,
                }
            if (
                isinstance(abs_diff, float)
                and isinstance(rel_diff, float)
                and (not math.isfinite(abs_diff) or not math.isfinite(rel_diff))
            ):
                return {
                    "status": "inconclusive",
                    "reason": "non_finite_numeric_delta",
                    "lhs": str(lhs_num),
                    "rhs": str(rhs_num),
                    "abs_diff": abs_diff,
                    "rel_diff": rel_diff,
                }
            return {
                "status": "conflict",
                "kind": "numeric",
                "lhs": str(lhs_num),
                "rhs": str(rhs_num),
                "abs_diff": abs_diff,
                "rel_diff": rel_diff,
                "difference_latex": render_latex(original_expr),
            }

        return {
            "status": "inconclusive",
            "reason": "non_real_or_symbolic_difference",
            "lhs": str(lhs),
            "rhs": str(rhs),
            "diff": str(diff),
        }
    except Exception as exc:
        return {
            "status": "inconclusive",
            "reason": "sympy_exception",
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
        }


def validate_reasoning_steps(eval_context: Any, expected_result: Any) -> dict[str, Any]:
    failures: list[dict[str, Any]] = []
    notes: list[dict[str, Any]] = []
    snapshots = getattr(eval_context, "snapshots", [])

    last_tree = None
    for index, snap in enumerate(snapshots):
        if not hasattr(snap, "original") or not hasattr(snap, "previous_tree"):
            text = str(getattr(snap, "text", ""))
            if "None" in text:
                failures.append(
                    {
                        "index": index,
                        "type": "text_contains_none",
                        "text": text,
                    }
                )
            continue

        if contains(snap.previous_tree, snap.original) <= 0:
            failures.append(
                {
                    "index": index,
                    "type": "original_not_in_previous_tree",
                }
            )
            continue

        replayed = replace_sub(snap.previous_tree, snap.original, snap.portion)
        if replayed != snap.full_tree:
            equivalence = compare_with_sympy(replayed, snap.full_tree)
            if equivalence.get("status") == "equivalent":
                notes.append(
                    {
                        "index": index,
                        "type": "rewrite_structural_mismatch_equivalent",
                        "equivalence_kind": equivalence.get("kind"),
                    }
                )
            else:
                failures.append(
                    {
                        "index": index,
                        "type": "rewrite_mismatch",
                        "previous_tree": render_latex(snap.previous_tree),
                        "original": render_latex(snap.original),
                        "portion": render_latex(snap.portion),
                        "expected_full": render_latex(snap.full_tree),
                        "replayed_full": render_latex(replayed),
                    }
                )
        last_tree = snap.full_tree

    final_tree_note = None
    if last_tree is not None and last_tree != expected_result:
        final_tree_note = {
            "type": "final_tree_mismatch",
            "last_tree": render_latex(last_tree),
            "expected_result": render_latex(expected_result),
        }

    rendered = eval_context.render()
    if "None" in rendered:
        failures.append({"type": "rendered_explanation_contains_none"})

    return {
        "valid": len(failures) == 0,
        "failure_count": len(failures),
        "failures": failures,
        "notes": notes + ([final_tree_note] if final_tree_note is not None else []),
        "rendered_length": len(rendered),
    }
