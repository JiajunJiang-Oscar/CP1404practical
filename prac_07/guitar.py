class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name = "", year = 0, cost = 0):
        """Initialise a Guitar instance.

        year, cost default as 0
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        """Do compare with year in list, return boolean"""
        return self.year < other.year

    def __str__(self):
        """Set up a format for output"""
        return f"{self.name:<25} ({self.year}) :${self.cost}"

