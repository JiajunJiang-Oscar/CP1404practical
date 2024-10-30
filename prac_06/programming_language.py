"""
Programming language
Estimate: 20 minutes
Actual:   15 minutes
"""
class ProgrammingLanguage:
    """Represent a ProgramLanguage object"""

    def __init__(self, language, typing, reflection, year):
        """Initialise a ProgramLanguage instance."""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check the typing equal to dynamic or not then return Ture if is dynamic"""
        return self.typing == 'dynamic'

    def __str__(self):
        """Set up a format for output"""
        return f"{self.language}, {self.typing} Typing, Reflection = {self.reflection}, First append in {self.year}"

