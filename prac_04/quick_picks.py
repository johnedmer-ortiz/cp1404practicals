import random

quick_picks = []
number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    quick_picks.append(tuple(random.randint(1, 45) for number in range(6)))

