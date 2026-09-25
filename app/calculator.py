def _to_float(value: object, field: str) -> float:
    """Convert *value* to float, raising TypeError for non-numeric types."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            f"Field '{field}' must be a numeric type, got {type(value).__name__!r}."
        )
    return float(value)


def process_user_data(data: dict) -> float:
    """
    Processes the user payload and calculates the final score.

    Defaults:
    - 'score' defaults to 0.0 if missing.
    - 'multiplier' defaults to 1.0 if missing.

    Raises:
        TypeError: if 'score' or 'multiplier' is present but not a numeric type.
    """
    raw_score = _to_float(data.get("score", 0.0), "score")
    multiplier = _to_float(data.get("multiplier", 1.0), "multiplier")

    return raw_score * multiplier


def calculate_bonus(base_points: float, bonus_factor: float) -> float:
    """
    Calculates bonus points.
    """
    if bonus_factor == 0:
        raise ZeroDivisionError("Bonus factor cannot be zero.")
    return base_points * bonus_factor