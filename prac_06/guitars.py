"""
CP1404 - prac_06 guitars
"""

from guitar import Guitar

print("My guitars!")

guitars = []

name = input("Name: ")
if name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))

while name != "":

    name = input("Name: ")
    if name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))


