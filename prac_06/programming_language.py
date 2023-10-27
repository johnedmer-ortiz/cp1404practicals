"""
CP1404 - prac_06 programming languages
Estimated time to finish: 40 mins
Actual:
"""

class ProgrammingLanguage:
    """Represents a programming language"""

    def __init__(self, language, typing, reflection, year):
        """Initialises language instance"""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns programming language typing"""
        return self.reflection
