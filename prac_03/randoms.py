"""
CP1404 - prac_03 - random numbers
"""
# print(random.randint(5, 20))
# What did you see on line 1? it printed random numbers from 5 to 20
# What was the smallest number you could have seen? smallest is 5
# what was the largest? largest is 20

# print(random.randrange(3, 10, 2))
# What did you see on line 2? it printed values 3, 5, 7 and 9
# What was the smallest number you could have seen? smallest is 3
# what was the largest? largest is 9
# Could line 2 have produced a 4? no, the code has a step distance of 2, the number 4 is skipped

# print(random.uniform(2.5, 5.5))
# What did you see on line 3? it printed random floats at a range of 2.5, 5.5 inclusive
# What was the smallest number you could have seen? help() says 2.5
# What was the largest? help() says 5.5

import random

print(random.uniform(1, 100))  # prints a random float from 1 to 100 inclusive
