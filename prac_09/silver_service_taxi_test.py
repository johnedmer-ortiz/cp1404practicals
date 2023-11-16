"""
CP1404 - prac09 - silver_service_taxi_test
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    test_taxi = SilverServiceTaxi("Limo", 150, 2)
    print(test_taxi)
    test_taxi.drive(18)
    print(test_taxi)
    print(f"Fare after drive: {test_taxi.get_fare()}")


main()
