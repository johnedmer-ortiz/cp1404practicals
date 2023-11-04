"""
CP1404 - prac_07_feedback - project_management.py
Estimated finish time: 2 hours
Actual finish time:
"""

from project import Project


def main():
    """Main function. Program starting point"""
    display_menu()
    menu_input = get_menu_input()
    while menu_input != "":
        if menu_input == "L":
            print("Test")

def display_menu():
    """Displays menu"""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def get_menu_input():
    """Prompts user for menu input"""
    return input(">>> ").upper()


main()
