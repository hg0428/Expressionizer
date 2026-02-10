import math
from decimal import Decimal, InvalidOperation


DEFAULT_SIGNIFICANT_DIGITS = 15


def _canonical_input(value: int | float, significant_digits: int) -> str:
    if isinstance(value, int):
        return str(value)
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
