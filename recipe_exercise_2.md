# Estimate time Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature
```python
def check_grammar(text)

    """
    
    parameters: 
        text: a string containing words

    returns:
        string if grammar is correct 'No grammatical errors'

        string if grammar is incorrect 'gramatical errors found in text'

    side effects:
        none    
        
        """

    pass    
```

## 3. Create Examples as Tests

argument - string with capital letter at start of text - 'Example string.'
returns - 'No grammatical errors'

argument - string with no capital letter at start of text - 'example string.'
returns - 'gramatical errors found in text'

argument - string with full stop at end of text - 'Example string.'
returns - 'No grammatical errors'

argument - string with letter at end of text - 'Example string'
returns - 'gramatical errors found in text'

argument - string wih exclamation mark at end of text - 'Example text!'
returns - 'No grammatical errors'

argument - string with incorrect punctuation at end of text - 'Example string&'
returns - 'Gramatical errors found in text'


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
