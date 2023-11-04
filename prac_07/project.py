"""
CP1404 - prac_07_feedback - project.py
"""


class Project:
    """Represents a project"""

    def __init__(self, name, start_date, priority, cost, completion_percent):
        """Initialises fields at object creation"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percent = completion_percent

    def __lt__(self, project):
        """overloads < operator for sort() function"""
        return self.priority < project.priority
