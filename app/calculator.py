def _to_float(value, field: str) -> float:
    """Cast *value* to float, raising TypeError for non-numeric inputs."""
    try:
        return float(value)
    except (ValueError, TypeError) as exc:
        raise TypeError(
            f"'{field}' must be numeric, got {type(value).__name__!r}: {value!r}"
        ) from exc


def process_user_data(data: dict) -> float:
    """
    Processes payload and calculates user score.

    Defaults:
      - 'score'      → 0.0  (missing key)
      - 'multiplier' → 1.0  (missing key)

    Raises TypeError if either value is present but non-numeric.
    """
    raw_score = _to_float(data.get("score", 0.0), "score")
    multiplier = _to_float(data.get("multiplier", 1.0), "multiplier")
    return raw_score * multiplier