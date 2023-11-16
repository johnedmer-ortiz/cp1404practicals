"""
CP1404 - prac09 - silver_service_taxi
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness, flagfall):
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km
        self.flagfall = flagfall
