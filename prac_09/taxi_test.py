"""
CP1404 - prac_09 taxi_test
"""

from taxi import Taxi


def main():
    """Main function for testing Taxi subclass"""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    # initialises the first two parameters using Car class
    # initialises the third parameter using taxi subclass

    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.current_fare_distance = 0
    print(my_taxi)
    my_taxi.drive(100)
    print(my_taxi)


main()
