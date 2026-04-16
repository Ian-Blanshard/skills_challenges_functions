import math
class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_to = 0

    def format(self):
        return f'{self.title.capitalize()}: {self.contents}'
    
    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())

    def reading_time(self, wpm):
        return math.ceil(len(self.format().split()) / wpm)

    def reading_chunk(self, wpm, minutes):
        amount_to_read = wpm * minutes
        if self.read_to >= len(self.title.split()) + len(self.contents.split()):
            self.read_to = 0
        chunk = ' '.join(self.format().split()[self.read_to:self.read_to + amount_to_read])
        self.read_to += wpm * minutes
        return chunk

