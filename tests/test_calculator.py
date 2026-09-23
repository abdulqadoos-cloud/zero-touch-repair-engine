import pytest
from app.calculator import process_user_data

def test_process_user_data_valid():
    payload = {"score": 10, "multiplier": 2}
    assert process_user_data(payload) == 20.0

def test_process_user_data_missing_key():
    # Test that will fail until IBM Bob 2.0 applies the fix
    payload = {"multiplier": 2}
    assert process_user_data(payload) == 0.0