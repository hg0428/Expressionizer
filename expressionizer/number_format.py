import math
from decimal import Decimal, InvalidOperation


DEFAULT_SIGNIFICANT_DIGITS = 15


def _format_large_int_fallback(value: int, significant_digits: int) -> str:
    if value == 0:
        return "0"
    sign = "-" if value < 0 else ""
    magnitude = abs(value)

    # Estimate decimal exponent from bit length.
    exponent = int((magnitude.bit_length() - 1) * math.log10(2))
    power = 10**exponent
    while magnitude >= power * 10:
        exponent += 1
        power *= 10
    while magnitude < power:
        exponent -= 1
        power //= 10

    # Build a compact scientific representation with stable significant digits.
    leading_scale = max(exponent - max(significant_digits - 1, 0), 0)
    leading = magnitude // (10**leading_scale)
    if leading_scale > 0:
        coefficient = leading / (10 ** (significant_digits - 1))
    else:
        coefficient = float(leading)
    coefficient_text = format(coefficient, f".{max(significant_digits - 1, 1)}g")
    return f"{sign}{coefficient_text}e{exponent}"


def _canonical_input(value: int | float, significant_digits: int) -> str:
    if isinstance(value, int):
        try:
            return str(value)
        except ValueError:
            return _format_large_int_fallback(value, significant_digits)
    if not math.isfinite(value):
        return str(value)
    return format(value, f".{significant_digits}g")


def to_trimmed_decimal_string(
    value: int | float,
    significant_digits: int = DEFAULT_SIGNIFICANT_DIGITS,
    min_value: float | None = None,
) -> str:
    """Return a stable decimal string without trailing zeros."""
    if min_value is not None and abs(value) < min_value:
        return "0"

    if isinstance(value, float) and not math.isfinite(value):
        return str(value)

    canonical = _canonical_input(value, significant_digits)
    try:
        normalized = format(Decimal(canonical), "f")
    except InvalidOperation:
        return canonical

    if "." in normalized:
        normalized = normalized.rstrip("0").rstrip(".")
    if normalized in ("", "-0"):
        return "0"
    return normalized
