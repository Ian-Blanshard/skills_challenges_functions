class GrammarStats:
    def __init__(self):
        self.failed_checks = 0
        self.passed_checks = 0

    def check(self, text):
        if type(text) != str:
            raise Exception('Invalid input, text must be a string')
        if text[0].isupper() and text[-1] in ('.', '!'):
            self.passed_checks += 1
            return True
        self.failed_checks += 1
        return False

    def percentage_good(self):
        return self.passed_checks / (self.passed_checks + self.failed_checks) * 100 if any((self.passed_checks, self.failed_checks)) else None