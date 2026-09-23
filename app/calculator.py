def process_user_data(data: dict) -> float:
    """
    Processes payload and calculates user score.
    Contains an intentional KeyError bug when 'score' key is missing.
    """
    # Intentional Bug: Direct key access causes KeyError if key isn't passed
    raw_score = data["score"] 
    multiplier = data.get("multiplier", 1.0)
    return float(raw_score * multiplier)