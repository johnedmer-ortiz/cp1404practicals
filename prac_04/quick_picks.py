"""
CP1404 quick picks generator
"""

import random

quick_picks = []  # storage for evaluated lists
number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    unique_numbers = []  # storage for list of unique numbers
    while len(unique_numbers) != 6:  # this loop block is for checking repetition and length of the list(checking block)
        random_numbers = [random.randint(1, 45) for j in range(6)]
        unique_numbers = [number for number in random_numbers if number not in unique_numbers]
    quick_picks.append(tuple(
        sorted(unique_numbers)))  # adds tuples(converted from lists) that passes the requirements to quick_picks array

quick_picks = tuple(quick_picks)  # converts the quick_picks list itself to tuple

for picks in quick_picks:  # loop to display the formatted picks
    print(" ".join(f"{number: 3}" for number in picks))
