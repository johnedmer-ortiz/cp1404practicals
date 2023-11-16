"""
CP1404 - prac09 - taxi_simulator
"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    taxis = create_taxis()


def create_taxis():
    taxis = [Taxi("Commodore", 100), SilverServiceTaxi("Mustang", 100, 5), SilverServiceTaxi("Corvette", 200, 8)]
    return taxis


main()
