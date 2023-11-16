"""
CP1404 - prac_09 unreliable_car
"""

import random

from car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Overrides Car __init__ method and inherits first two parameters"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Try drive the car for a specific distance"""
        if random.randint(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
        else:
            print("Unable to drive.")
        return distance
