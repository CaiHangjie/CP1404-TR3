"""
Estimate: 5 h
Actual:    1 day
"""


import csv
from project import Project
from datetime import datetime


def load_projects(filename="projects.txt"):
    """Load projects from a file and return """
    projects = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        next(csv_reader)  # Skip header
        for row in csv_reader:
            name, start_date, priority, cost_estimate, completion_percentage = row
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    """Save Project objects"""
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter='\t')
        csv_writer.writerow(['Name', 'Start Date', 'Priority', 'Cost Estimate', 'Completion Percentage'])
        for project in projects:
            csv_writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'),
                                 project.priority, project.cost_estimate, project.completion_percentage])

    print(f"Saved projects to {filename}")


def display_projects(projects):
    """Sort based on priority or status"""
    incomplete_projects = sorted([p for p in projects if not p.is_completed()], key=lambda p: p.priority)
    completed_projects = sorted([p for p in projects if p.is_completed()], key=lambda p: p.priority)

    print("\nIncomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Sorted by start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = sorted([p for p in projects if p.start_date > filter_date], key=lambda p: p.start_date)

        print("\nFiltered projects:")
        for project in filtered_projects:
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please enter in dd/mm/yyyy.")


def add_new_project(projects):
    """Add a new project """
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print(f"Added new project: {new_project}")


def update_project(projects):
    """Update project"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        project_index = int(input("Project choice: "))
        selected_project = projects[project_index]

        new_completion = input("New completion percentage : ")
        new_priority = input("New priority : ")

        if new_completion:
            selected_project.completion_percentage = int(new_completion)
        if new_priority:
            selected_project.priority = int(new_priority)
        print(f"Updated project: {selected_project}")

    except (ValueError, IndexError):
        print("Invalid")


def main():
    """Main program to manage projects."""
    filename = 'projects.txt'
    projects = load_projects(filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {filename}")

    while True:
        # Display menu
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").strip().upper()

        if choice == 'L':
            filename = input("Enter filename to load projects from: ")
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print(f"File {filename} not found.")
        elif choice == 'S':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Saved projects to {filename}")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            # Save to the default file if the user agrees
            if input("Would you like to save to projects.txt? (y/n): ").strip().lower() == 'y':
                save_projects('projects.txt', projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


main()
