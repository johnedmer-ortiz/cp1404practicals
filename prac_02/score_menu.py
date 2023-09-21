"""
Score menu - prac02
"""


def main():
    """Main function, execute functions calls depending on choice"""
    choice = ""
    score = get_valid_score()
    while choice != "Q":
        display_menu()
        choice = get_choice()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            get_remark(score)
        elif choice == "S":
            display_stars(score)
        elif choice == "Q":
            display_goodbye()
        else:
            display_invalid_input()


def display_menu():
    """Displays menu"""
    print("""(G)et score
(P)rint result
(S)how stars
(Q)uit""")


def display_goodbye():
    """Displays exit message"""
    print("Goodbye.")


def display_invalid_input():
    """Handles unrecognised choice input"""
    print("Invalid input. Try again.")


def display_stars(score):
    """prints number of * equal to score"""
    print("*" * score)


def get_valid_score():
    """prompts user for score input and returns it"""
    score = -1
    score = int(input("Enter score:"))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score:"))
    return score


def get_choice():
    """>> input prompt indicator, returns character choice"""
    choice = input(">>")
    return choice.upper()


def get_remark(score):
    """Evaluates score and displays corresponding remark string"""
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
