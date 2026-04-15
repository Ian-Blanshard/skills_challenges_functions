def make_snippet(string):
    if type(string) != str:
        raise Exception('Input is not a string')
    return string if len(string.split()) <= 5 else ' '.join(string.split()[:5]) + ' ...'

def count_words():
    pass