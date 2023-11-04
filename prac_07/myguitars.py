"""
CP1404 - prac_07_feedback - myguitars.py
"""

from guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    """Main function. Program starting point"""
    my_guitars = read_guitars()
    sort_guitars(my_guitars)
    display_guitars(my_guitars)


def display_guitars(my_guitars):
    """Display guitars and details"""
    for guitar in my_guitars:
        print(guitar)


def read_guitars():
    """Reads csv file into objects"""
    my_guitars = []
    with open(FILE_NAME, "r") as in_file:
        for line in in_file:
            guitar = line.strip().split(",")
            my_guitars.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
    return my_guitars


def sort_guitars(my_guitars):
    """Sorts guitars by year"""
    my_guitars.sort()


main()
