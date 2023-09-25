"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("You cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")

# 1. ValueError occurs when either of the two inputs are not valid numbers
# 2. ZeroDivisionError occurs when zero denominator will avoid the possibility of ZeroDivisionError
# 3. An if block that checks and handles zero denominators will eliminate the need for the ZeroDivisionError except block
