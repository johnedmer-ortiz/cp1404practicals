"""
CP1404 - unreliable_car_test
"""
from unreliable_car import UnreliableCar


def main():
    bad_car = UnreliableCar("Subaru", 120, 40)
    print(bad_car)
    bad_car.drive(20)
    print(bad_car)


main()
