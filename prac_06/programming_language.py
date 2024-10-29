"""
Programming language
Estimate:  minutes
Actual:    minutes
"""
class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == 'dynamic'

    def __str__(self):
        return f"{self.language}, {self.typing} Typing, Reflection = {self.reflection}, First append in {self.year}"

