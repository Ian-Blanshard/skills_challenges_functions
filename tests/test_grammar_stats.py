from lib.grammar_stats import *
import pytest

def test_check_for_starting_capital_end_char():
    grammar_check = GrammarStats()
    assert grammar_check.check('My test text') == False

def test_check_for_starting_not_capital_end_exclamation_mark():
    grammar_check = GrammarStats()
    assert grammar_check.check('my test text!') == False

def test_check_for_starting_capital_end_full_stop():
    grammar_check = GrammarStats()
    assert grammar_check.check('My test text.') == True

def test_check_for_starting_capital_end_exclamation_mark():
    grammar_check = GrammarStats()
    assert grammar_check.check('My test text!') == True

def test_check_for_starting_capital_end_colon():
    grammar_check = GrammarStats()
    assert grammar_check.check('My test text:') == False

def test_check_for_non_valid_input():
    grammar_check = GrammarStats()
    with pytest.raises(Exception) as error:
        grammar_check.check(1)
    error_message = str(error.value)
    assert error_message == 'Invalid input, text must be a string'

def test_percentage_good_for_all_good_texts():
    grammar_check = GrammarStats()
    grammar_check.check('My test text!')
    grammar_check.check('My test text.')
    assert grammar_check.percentage_good() == 100

def test_percentage_good_for_half_good_texts():
    grammar_check = GrammarStats()
    grammar_check.check('My test text!')
    grammar_check.check('My test text')
    assert grammar_check.percentage_good() == 50

def test_percentage_good_for_75percent_good_texts():
    grammar_check = GrammarStats()
    grammar_check.check('My test text!')
    grammar_check.check('My test text!')
    grammar_check.check('My test text!')
    grammar_check.check('My test text')
    assert grammar_check.percentage_good() == 75



