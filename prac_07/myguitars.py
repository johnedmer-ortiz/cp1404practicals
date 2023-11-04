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
    add_guitars(my_guitars)
    sort_guitars(my_guitars)
    display_guitars(my_guitars)
    save_guitars(my_guitars)


def save_guitars(my_guitars):
    """Updates guitars.csv file"""
    with open(FILE_NAME, "w") as out_file:
        for guitar in my_guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def add_guitars(my_guitars):
    """Adds guitar(s) to guitar object list"""
    print("Adding guitar(s)...")
    name = input("Name: ")
    if name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        my_guitars.append(Guitar(name, year, cost))

    while name != "":
        name = input("Name: ")
        if name != "":
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            my_guitars.append(Guitar(name, year, cost))


def display_guitars(my_guitars):
    """Display guitars and details"""
    print("---My Guitars---")
    for guitar in my_guitars:
        print(guitar)
    print("----------------")


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
