import math

def estimate_time(string):

    if type(string) != str:
        raise Exception('Input is not a string')

    minutes = math.ceil(len(string.split()) / 200)
    hours, minutes = divmod(minutes, 60)

    if hours:
        if hours == 1:
            if minutes == 1:
                return f'{hours} hour and {minutes} minute'
            return f'{hours} hour and {minutes} minutes'
        if minutes == 1:
            return f'{hours} hours and {minutes} minute'
        return f'{hours} hours and {minutes} minutes'
    
    if minutes == 1:
        return f'{minutes} minute'
    return f'{minutes} minutes'