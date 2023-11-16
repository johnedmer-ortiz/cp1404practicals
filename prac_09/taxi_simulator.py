"""
CP1404 - prac09 - taxi_simulator
"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

TAXI_CHOICES = ("q)uit, c)hoose taxi, d)rive"
                ">>> ")


def main():
    print("Let's drive!")
    taxis = create_taxis()
    customer_choice = input(TAXI_CHOICES).upper()
    while customer_choice != "Q":
        if customer_choice == "C":
            display_taxis(taxis)
        customer_choice = input(TAXI_CHOICES).upper()


def create_taxis():
    taxis = [Taxi("Commodore", 100), SilverServiceTaxi("Mustang", 100, 5), SilverServiceTaxi("Corvette", 200, 8)]
    return taxis


def select_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
