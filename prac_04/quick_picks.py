import random

quick_picks = []
number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    random_numbers = [random.randint(1, 45) for i in range(6)]
    unique_numbers = []
    while len(unique_numbers) != 6:
        unique_numbers = [number for number in random_numbers if number not in unique_numbers]

    #print(str(quick_picks[i]).strip("()"))
