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
        """Returns guitar details"""
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        """Returns age of guitar relative to year 2023"""
        return 2023 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        return False
