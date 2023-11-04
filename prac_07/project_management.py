"""
CP1404 - prac_07_feedback - project_management.py
Estimated finish time: 2 hours
Actual finish time:
"""

from project import Project


def main():
    """Main function. Program starting point"""

    projects = []
    display_menu()
    menu_input = get_menu_input()
    while menu_input != "":
        if menu_input == "L":
            load_project()
        elif menu_input == "S":
            print("test save")
        menu_input = get_menu_input()


def load_project(projects):
    """Reads projects from chosen txt file"""
    file_name = input("Enter project file name: ")
    with open(file_name, "r") as in_file:
        in_file.readline()
        for line in in_file:
            project = line.strip().split("\t")
            projects.append(Project(project[0], project[1], project[2], project[3], project[4]))


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
