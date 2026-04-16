from lib.exercise_1 import *
import pytest
def test_estimate_time_empty_string():
    assert estimate_time('') == '0 minutes'

def test_estimate_time_199_string():
    text = 'word ' * 199
    assert estimate_time(text) == '1 minute'

def test_estimate_time_200_string():
    text = 'word ' * 201
    assert estimate_time(text) == '2 minutes'

def test_estimate_time_12201_string():
    text = 'word ' * 12200
    assert estimate_time(text) == '1 hour and 1 minute'

def test_estimate_time_12202_string():
    text = 'word ' * 12202
    assert estimate_time(text) == '1 hour and 2 minutes'

def test_estimate_time_24002_string():
    text = 'word ' * 24002
    assert estimate_time(text) == '2 hours and 1 minute'

def test_estimate_time_24202_string():
    text = 'word ' * 24202
    assert estimate_time(text) == '2 hours and 2 minutes'

def test_estimate_time_none_string():
    with pytest.raises(Exception) as error:
        assert estimate_time([1,2,3]) 
    error_message = str(error.value)
    assert error_message == 'Input is not a string'