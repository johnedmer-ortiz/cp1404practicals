"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

print(f"{year} {name} for about ${cost:,.0f}!")

for i in range(0, 200, 50):
    print(f"{i:>3}")
