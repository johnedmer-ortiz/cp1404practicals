"""
CP1404 - prac_09 taxi_test
"""

from taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.current_fare_distance = 0
    print(my_taxi)
    my_taxi.drive(100)
    print(my_taxi)


main()
