from lib.personal_diary import *

######################## make_snippet tests ########################
"""
test a string of 5 is returned as they are
"""
def test_string_of_five():
    result = make_snippet('one two three four five')
    assert result == 'one two three four five'
""" 
test a string of >5 is returned with the first 5 and ...
"""
def test_string_of_greater_than_five():
    result = make_snippet('one two three four five six')
    assert result == 'one two three four five ...'
"""
test a string <5 is returned as they are
"""
def test_string_less_than_five():
    result = make_snippet('one two three four')
    assert result == 'one two three four'

######################### count_words tests #########################