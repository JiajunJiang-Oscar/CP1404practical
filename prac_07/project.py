"""
Project
Estimate: 30 minutes
Actual:   45 minutes
"""
import datetime
class Project:
    """Represent a Project object."""

    def __init__(self, name, date, priority = 0, cost = 0, completion_percentage = 0):
        """Initialise a Project instance.

        priority, cost, completion_percentage default as 0
        """
        self.name = name
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def is_complete(self):
        """Check completion percentage is equal to 100 or not, return boolean."""
        return self.completion_percentage == 100

    def string_changer(self):
        """Set up the format of write file method."""
        return f"{self.name}\t{self.date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost}\t{self.completion_percentage}"

    def __str__(self):
        """Set up a format for output."""
        return (f"{self.name}, start: {self.date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: {self.cost}, "
                f"completion: {self.completion_percentage}%")