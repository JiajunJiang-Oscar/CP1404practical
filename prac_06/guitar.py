"""
Guitar
Estimate: 20 minutes
Actual:   27 minutes
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name = "", year = 0, cost = 0):
        """Initialise a Guitar instance.

        year, cost default as 0
        """
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """calculate the age of the guitar."""
        current_year = 2024
        age = current_year - self.year
        return age

    def is_vintage(self):
        """Determine if the guitar age is in range or not."""
        return self.get_age() >= 50

    def __str__(self):
        """Set up a format for output"""
        return f"{self.name} ({self.year}) :${self.cost}"
