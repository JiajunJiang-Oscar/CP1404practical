from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability and new drive method."""

    def __init__(self, name, fuel):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)

        # Set the reliability to the value passed in
        self.reliability = float(randint(0, 100))

    def drive(self, distance):
        """Drive the car a given distance if it is reliable enough."""

        # Only drive if a random number is less than the reliability.
        if distance < self.reliability:
            return super().drive(distance)
        return 0

