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
        if self.typing == "Dynamic":
            return True
        return False

    def __str__(self):
        """Returns a string of information about the programming language"""
        return f"{self.language}, {self.typing} Typing, First appeared in {self.year}"