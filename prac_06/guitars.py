"""
CP1404 - prac_06 guitars
"""

from guitar import Guitar

print("My guitars!")

guitars = []

name = input("Name: ")
year = int(input("Year: "))
cost = float(input("Cost: $"))

guitars.append(Guitar(name, year, cost))

