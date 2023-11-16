"""
CP1404 - prac09 - taxi_simulator
"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

TAXI_CHOICES = ("q)uit, c)hoose taxi, d)rive\n"
                ">>> ")


def main():
    """Directs inputs to appropriate methods"""
    print("Let's drive!")
    taxis = create_taxis()
    taxi_choice = ""
    fare = 0
    customer_choice = input(TAXI_CHOICES).upper()
    while customer_choice != "Q":
        if customer_choice == "C":
            taxi_choice = select_taxi(taxis, False)
        elif customer_choice == "D":
            if taxi_choice != "":
                fare += drive(taxis[taxi_choice])
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${fare:.2f}")
        customer_choice = input(TAXI_CHOICES).upper()
    exit_simulator(fare, taxis)


def create_taxis():
    """Initialises list of taxis"""
    taxis = [Taxi("Commodore", 100), SilverServiceTaxi("Mustang", 100, 2), SilverServiceTaxi("Corvette", 200, 3)]
    return taxis


def select_taxi(taxis, exit_flag):
    """Acquire taxi selection"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    if not exit_flag:
        return int(input("Choose taxi: "))


def drive(taxi):
    """Returns fare base on drive distance"""
    distance = int(input("Drive how far? "))
    taxi.drive(distance)
    print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")
    return taxi.get_fare()


def exit_simulator(fare, taxis):
    """Displays total trip details and update taxi kms"""
    print(f"Total trip cost: ${fare:.2f}")
    print("Taxis are now:")
    select_taxi(taxis, True)


main()
