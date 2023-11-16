"""
CP1404 - prac09 - silver_service_taxi
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness, flagfall):
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km
        self.flagfall = flagfall

    def get_fare(self):
        return (self.price_per_km * self.current_fare_distance) + self.flagfall

    def __str__(self):
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km "
                f"plus flagfall of ${self.flagfall}")
