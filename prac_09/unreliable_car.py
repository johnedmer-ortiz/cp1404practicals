"""
CP1404 - prac_09 unreliable_car
"""

from car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
