# Estimate time Function Design Recipe

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


## 2. Design the Function Signature
```python
def estimate_time(text)

    """
    
    parameters: 
        text: a string containing words

    returns:
        the estimated reading time of the text
        in minutes/hours

    side effects:
        none    
        
        """

    pass    
```

## 3. Create Examples as Tests

argument - empty string
returns - string: 0 minutes

arguement - string 199 words in length
returns - string: 1 minute

argument - string  201 words in length
returns - 2 minutes 

argument - string 12001 words in length
returns - string 1 hour and 1 minute 

argument - string 12201 words in length
returns - string 1 hour and 2 minutes 

argument - none string type
returns exception 'none string type passed as argument'


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
