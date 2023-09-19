from random import *


def main():
    """Grabs score from user input and prints remark"""
    score = float(input("Enter score: "))
    remark = get_remark(score)
    print(remark)
    score = randint(0, 100)
    print(f"Random score: {score}")
    remark = get_remark(score)
    print(remark)


def get_remark(score):
    """Evaluates score and allocates corresponding remark string"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
