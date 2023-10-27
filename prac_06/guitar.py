"""
CP1404 - prac_06 guitars
Estimated time to finish: 60 mins
Actual:
"""

class Guitars:
    """Represents a guitar"""
    def __init__(self, name="", year=0, cost=0):
        """Initialises guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost}"