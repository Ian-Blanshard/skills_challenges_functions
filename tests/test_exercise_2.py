from lib.exercise_2 import *

def test_capital_at_start():
    assert check_grammar('Example string.') == 'No grammatical errors'

def test_no_capital_at_start():
    assert check_grammar('example string.') == 'Gramatical errors found in text'

def test_full_stop_at_end():
    assert check_grammar('Example string.') == 'No grammatical errors'

def test_letter_at_end():
    assert check_grammar('Example string') == 'Gramatical errors found in text'

def test_exclamation_mark_at_end():
    assert check_grammar('Example string!') == 'No grammatical errors'

def test_incorrect_punctuation_at_end():
    assert check_grammar('Example string&') == 'Gramatical errors found in text'