"""
CP1404 - prac_07_feedback - myguitars.py
"""

from guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    """Main function. Program starting point"""
    my_guitars = read_guitars()


def read_guitars():
    """Reads csv file into objects"""
    my_guitars = []
    with open(FILE_NAME, "r") as in_file:
        for line in in_file:
            my_guitars.append(Guitar(line[0], line[1], line[2]))
    return my_guitars


main()
