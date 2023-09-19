def display_menu():
    print("""(G)et score
(P)rint result
(S)how stars
(Q)uit""")


def display_goodbye():
    print("Goodbye.")


def display_invalid_input():
    print("Invalid input. Try again.")


def display_stars(score):
    print("*" * score)


def get_score():
    score = float(input("Enter score:"))
    return score


def get_choice():
    choice = input(">>")
    return choice


def get_remark(score):
    """Evaluates score and allocates corresponding remark string"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def main():
    choice = ""
    score = 0
    while choice != "Q":
        display_menu()
        choice = get_choice()
        if choice == "G":
            score = get_score()
        elif choice == "P":
            get_remark(score)
        elif choice == "S":
            display_stars(score)
        else:
            display_invalid_input()


main()
