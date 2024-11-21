class Band:
    """Band class to manage a group of musicians."""
    def __init__(self, band_name):
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.band_name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to band"""
        self.musicians.append(musician)

    def play(self):
        """Return a string of all musicians playing their instruments."""
        return "\n".join(musician.play() for musician in self.musicians)