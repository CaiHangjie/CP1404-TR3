import random
from car import Car

class UnreliableCar(Car):
    """ Initialise an UnreliableCar instance."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        # generate a random number between 0 and 100, and only drive the car if that number is less than the car's reliability.
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0