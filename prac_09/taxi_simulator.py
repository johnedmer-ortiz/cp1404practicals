"""
CP1404 - prac09 - taxi_simulator
"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

TAXI_CHOICES = ("q)uit, c)hoose taxi, d)rive\n"
                ">>> ")


def main():
    print("Let's drive!")
    taxis = create_taxis()
    taxi_choice = ""
    customer_choice = input(TAXI_CHOICES).upper()
    while customer_choice != "Q":
        if customer_choice == "C":
            taxi_choice = select_taxi(taxis)
        print(f"Bill to date: ${calculate_bill(taxis[taxi_choice]):.2f}")
        customer_choice = input(TAXI_CHOICES).upper()


def create_taxis():
    taxis = [Taxi("Commodore", 100), SilverServiceTaxi("Mustang", 100, 5), SilverServiceTaxi("Corvette", 200, 8)]
    return taxis


def select_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    return int(input("Choose taxi: "))


def calculate_bill(taxi):
    return taxi.get_fare()


main()
