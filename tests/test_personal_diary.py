from lib.personal_diary import *
import pytest
######################## make_snippet tests ########################
"""
test a string of 5 is returned as they are
"""
def test_make_snippet_string_of_five():
    result = make_snippet('one two three four five')
    assert result == 'one two three four five'
""" 
test a string of >5 is returned with the first 5 and ...
"""
def test_make_snippet_string_of_greater_than_five():
    result = make_snippet('one two three four five six')
    assert result == 'one two three four five ...'
"""
test a string <5 is returned as they are
"""
def test_make_snippet_string_less_than_five():
    result = make_snippet('one two three four')
    assert result == 'one two three four'
"""
test an exception is raised if a integer is passed as argument
"""
def test_make_snippet_exception_for_integer():
    with pytest.raises(Exception) as error:
        make_snippet(5)
    error_message = str(error.value)
    assert error_message == 'Input is not a string'
"""
test an exception is raised if a boolean is passed as argument
"""
def test_make_snippet_exception_for_boolean():
    with pytest.raises(Exception) as error:
        make_snippet(True)
    error_message = str(error.value)
    assert error_message == 'Input is not a string'
"""
test an exception is raised if a list is passed as argument
"""
def test_make_snippet_exception_for_list():
    with pytest.raises(Exception) as error:
        make_snippet(['one', 'two'])
    error_message = str(error.value)
    assert error_message == 'Input is not a string'
"""
test an exception is raised if a dictionary is passed as argument
"""
def test_make_snippet_exception_for_dict():
    with pytest.raises(Exception) as error:
        make_snippet({'one': 'one', 'two': 'two'})
    error_message = str(error.value)
    assert error_message == 'Input is not a string'
"""
test an exception is raised if a tuple is passed as argument
"""
def test_make_snippet_exception_for_tuple():
    with pytest.raises(Exception) as error:
        make_snippet(('one', 'two'))
    error_message = str(error.value)
    assert error_message == 'Input is not a string'
######################### count_words tests #########################
""""
test"""