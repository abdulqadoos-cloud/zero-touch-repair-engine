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
    """
    # BUG INJECTED: Missing dictionary keys defaults ("score" and "multiplier") 
    # causing an unhandled KeyError when payloads omit these fields.
    raw_score = _to_float(data["score"], "score")
    multiplier = _to_float(data["multiplier"], "multiplier")
    
    # BUG INJECTED: Division by zero or logic error instead of multiplication
    return raw_score / 0.0