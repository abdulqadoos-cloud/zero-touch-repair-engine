import pytest
from app.calculator import process_user_data


# ---------------------------------------------------------------------------
# Happy-path
# ---------------------------------------------------------------------------

def test_process_user_data_valid():
    """Both keys present — standard multiplication."""
    payload = {"score": 10, "multiplier": 2}
    assert process_user_data(payload) == 20.0


def test_process_user_data_float_score():
    """Float score with float multiplier returns correct float."""
    payload = {"score": 2.5, "multiplier": 4.0}
    assert process_user_data(payload) == 10.0


def test_process_user_data_zero_score_explicit():
    """Explicit score of 0 (not the default) should return 0.0."""
    payload = {"score": 0, "multiplier": 5}
    assert process_user_data(payload) == 0.0


# ---------------------------------------------------------------------------
# Missing-key scenarios
# ---------------------------------------------------------------------------

def test_process_user_data_missing_score_key():
    """Missing 'score' key defaults to 0.0 — original regression test."""
    payload = {"multiplier": 2}
    assert process_user_data(payload) == 0.0


def test_process_user_data_missing_multiplier_key():
    """Missing 'multiplier' key defaults to 1.0, leaving score unchanged."""
    payload = {"score": 7}
    assert process_user_data(payload) == 7.0


def test_process_user_data_empty_payload():
    """Completely empty dict — both defaults kick in, result is 0.0."""
    assert process_user_data({}) == 0.0


# ---------------------------------------------------------------------------
# Non-numeric value inputs
# ---------------------------------------------------------------------------

def test_process_user_data_string_score_raises():
    """A string 'score' value cannot be multiplied to a float — TypeError."""
    payload = {"score": "high", "multiplier": 2}
    with pytest.raises(TypeError):
        process_user_data(payload)


def test_process_user_data_string_multiplier_raises():
    """A string 'multiplier' value cannot multiply a number — TypeError."""
    payload = {"score": 5, "multiplier": "two"}
    with pytest.raises(TypeError):
        process_user_data(payload)


def test_process_user_data_none_score_raises():
    """None as 'score' cannot be cast to float — TypeError."""
    payload = {"score": None}
    with pytest.raises(TypeError):
        process_user_data(payload)


def test_process_user_data_none_multiplier_raises():
    """None as 'multiplier' cannot multiply a number — TypeError."""
    payload = {"score": 3, "multiplier": None}
    with pytest.raises(TypeError):
        process_user_data(payload)