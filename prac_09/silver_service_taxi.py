"""
CP1404 - prac09 - silver_service_taxi
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represents silver service taxi"""

    def __init__(self, name, fuel, fanciness):
        """Initialises silver service instance and inherits first two parameters"""
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km
        self.flagfall = 4.50

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Drive like Car class but calculate fare distance as well."""
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km "
                f"plus flagfall of ${self.flagfall:.2f}")
