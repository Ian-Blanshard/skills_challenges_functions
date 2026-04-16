def check_grammar(string):
    if string[0].isupper() and string[-1] in ('!', '.'):
        return 'No grammatical errors'
    return 'Gramatical errors found in text'