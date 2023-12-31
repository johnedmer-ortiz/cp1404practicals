"""
CP1404 - prac_07_feedback - project_management.py
Estimated finish time: 2 hours
Actual finish time: 5 hours 36 minutes
"""

from project import Project
from datetime import datetime


def main():
    """Main function. Program starting point"""
    projects = []
    display_menu()
    menu_input = get_menu_input()
    while menu_input != "Q":
        if menu_input == "L":
            load_project(projects)
        elif menu_input == "S":
            save_project(projects)
        elif menu_input == "D":
            display_projects(projects)
        elif menu_input == "F":
            filter_by_date(projects)
        elif menu_input == "A":
            add_project(projects)
        elif menu_input == "U":
            update_project(projects)
        else:
            print("Invalid menu choice. Try again.")
        display_menu()
        menu_input = get_menu_input()
    print("Thank you for using custom-built project management software.")


def update_project(projects):
    """Updates completion percent and priority of a project"""
    for i, project in enumerate(projects):
        print(f"{i} {project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.cost}, completion: {project.completion_percent}%")

    bad_choice = True
    while bad_choice:
        try:
            choice = int(input("Project choice: "))
            if choice > len(projects) or choice < 0:
                print("Project choice not in the the list. Try again.")
                continue
            bad_choice = False
        except ValueError:
            print("Project choice input not an integer. Try again.")

    print(f"{projects[choice].name}, start: {projects[choice].start_date}, priority {projects[choice].priority}, "
          f"estimate: ${projects[choice].cost}, completion: {projects[choice].completion_percent}%")
    projects[choice].completion_percent = float(input("New Percentage: "))
    projects[choice].priority = int(input("New Priority: "))


def add_project(projects):
    """Add project to projects object list"""
    print("Let's add a new project")
    bad_project_details = True
    while bad_project_details:
        try:
            name = input("Project name: ")
            start_date = input("Start date (dd/mm/yyyy): ")
            priority = int(input("Priority: "))
            cost = float(input("Cost estimate: $"))
            completion_percent = float(input("Percent complete: "))
            projects.append(Project(name, start_date, priority, cost, completion_percent))
            bad_project_details = False
        except ValueError:
            print("Invalid project info. Try again.")


def filter_by_date(projects):
    """Filters projects by date"""
    bad_date = True
    while bad_date:
        try:
            filter_date = input("Show projects that start after date (dd/mm/yy): ")
            date_format = "%d/%m/%Y"
            filter_date = datetime.strptime(filter_date, date_format)
            bad_date = False
        except ValueError:
            print("Invalid date. Try Again")

    filtered = [project for project in projects if datetime.strptime(project.start_date, date_format) > filter_date]
    for project in filtered:
        project.sort_flag = "date"
        project.start_date = datetime.strptime(project.start_date, date_format)
    filtered.sort()

    for project in filtered:
        project.start_date = str(project.start_date.strftime(date_format))
        print(f"\t{project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.cost}, completion: {project.completion_percent}%")


def display_projects(projects):
    """Displays completed and uncompleted projects"""
    unfinished_projects, finished_projects = sort_projects(projects)
    print("Incomplete projects:")
    for project in unfinished_projects:
        print(f"\t{project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.cost}, completion: {project.completion_percent}%")
    print("Completed projects:")
    for project in finished_projects:
        print(f"\t{project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.cost}, completion: {project.completion_percent}%")


def sort_projects(projects):
    """Sorts projects by completion and priority"""
    for project in projects:
        project.sort_flag = "priority"
    unfinished_projects = [project for project in projects if int(project.completion_percent) < 100]
    finished_projects = [project for project in projects if project not in unfinished_projects]
    unfinished_projects.sort()
    finished_projects.sort()
    return unfinished_projects, finished_projects


def load_project(projects):
    """Reads projects from chosen txt file"""
    bad_file_name = True
    while bad_file_name:
        try:
            file_name = input("Enter project file name: ")
            with open(file_name, "r") as in_file:
                in_file.readline()
                for line in in_file:
                    project = line.strip().split("\t")
                    projects.append(Project(project[0], project[1], int(project[2]), project[3], float(project[4])))
            bad_file_name = False
        except FileNotFoundError:
            print("File not found. Try again.")
    print(f"Project loaded from {file_name}")


def save_project(projects):
    """Saves project to a text file"""
    bad_save_file = True
    while bad_save_file:
        try:
            file_name = input("Enter project file name: ")
            with open(file_name, "w") as out_file:
                out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
                for project in projects:
                    out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}"
                                   f"\t{project.cost}\t{project.completion_percent}\n")
            bad_save_file = False
        except FileNotFoundError:
            print("Invalid save file name. Try again.")
    print(f"Projects saved to {file_name}")


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
