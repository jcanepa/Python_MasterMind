import random


class CodeMaker:

    code = []
    colors = []
    length = 4

    def __init__(self, code_length, colors):
        self.code_length = code_length
        self.colors = colors
        self.set_code()

    def set_code(self):
        i = 1
        while i <= self.code_length:
            self.code.append(random.choice(self.colors))
            i += 1

    def get_code(self):
        return self.code
