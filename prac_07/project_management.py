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
            file_in = load_project()
            file_in.close()
        menu_input = get_menu_input()


def load_project():
    """Reads projects from chosen txt file"""
    file_name = input("Enter project file name: ")
    file_in = open(file_name, "r")
    print(f"Projects from {file_name} loaded.")
    return file_in


def save_project():
    """Saves project to a text file"""
    file_name = input("Enter project file name: ")
    file_out = open(file_name, "w")
    print(f"Projects saved to {file_name}")
    file_out.close()


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
