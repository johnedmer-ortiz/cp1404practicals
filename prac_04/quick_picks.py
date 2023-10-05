import random

quick_picks = []
number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    unique_numbers = []
    while len(unique_numbers) != 6:
        random_numbers = [random.randint(1, 45) for j in range(6)]
        unique_numbers = [number for number in random_numbers if number not in unique_numbers]
    quick_picks.append(tuple(sorted(unique_numbers)))

quick_picks = tuple(quick_picks)

for picks in quick_picks:
    print(str(picks).strip("()"))
