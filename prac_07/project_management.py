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
            load_project(projects)
        elif menu_input == "S":
            print("test save")
        elif menu_input == "D":
            display_projects(projects)
        menu_input = get_menu_input()


def display_projects(projects):
    """Displays completed and uncompleted projects"""
    unfinished_projects, finished_projects = sort_completion(projects)
    print("Incomplete projects:")
    for project in unfinished_projects:
        print(
            f"- {project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost}, completion: {project.completion_percent}%")
    print("Completed projects:")
    for project in finished_projects:
        print(
            f"- {project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost}, completion: {project.completion_percent}%")


def sort_completion(projects):
    """Sorts projects by completion and priority"""
    unfinished_projects = [project for project in projects if int(project.completion_percent) < 100]
    finished_projects = [project for project in projects if project not in unfinished_projects]
    unfinished_projects.sort()
    finished_projects.sort()
    return unfinished_projects, finished_projects


def load_project(projects):
    """Reads projects from chosen txt file"""
    file_name = input("Enter project file name: ")
    with open(file_name, "r") as in_file:
        in_file.readline()
        for line in in_file:
            project = line.strip().split("\t")
            projects.append(Project(project[0], project[1], int(project[2]), project[3], float(project[4])))
    print(f"Project loaded from {file_name}")


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
