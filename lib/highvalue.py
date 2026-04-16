# File: lib/high_value.py

class HighValue:
    # create an instance  create two values 1st and 2nd
    def __init__(self, value_first, value_second):
        self.value_first = value_first
        self.value_second = value_second

    # tests which of the two values are highest or if they are equal  returns string 
    def get_highest(self):
        if self.value_first > self.value_second:
            return "First value is higher"
        elif self.value_first < self.value_second:
            return "Second value is higher"
        else:
            return "Values are equal"
        
    # we pass a value to the method if first one increase that or if second increase second
    def add(self, increase_by, selection):
        if selection == "first":
            self.value_first += increase_by
        elif selection == "second":
            self.value_second += increase_by
