"""
Project Management
Estimate: 2 hours
Actual:   2.5 hours
"""

from prac_07.project import Project
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by dat\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")

def main():
    file_name = "projects.txt"
    datas = read_file(file_name)
    print(f"Welcome to Pythonic Project Management"
          f"\nLoaded {len(datas)} projects from {file_name}.")

    choice = input(f"{MENU}\n>>>").upper()
    while choice != "Q":
        if choice == "L":

            # Get a new file name and load information in that file
            new_file_name = input("Please enter file name\n>>>")
            datas = read_file(new_file_name)

        elif choice == "S":

            # Get a new file name and save the data in that file
            save_name = input(f"Please enter file name\n>>>")
            save_data(datas, save_name)
            print("Data save successfully")

        elif choice == "D":
            show_data(datas)

        elif choice == "F":
            latter_project = date_check(datas)
            for data in latter_project:
                print(data)

        elif choice == "A":
            print("Let's add a new project")
            add_data(datas)

        elif choice == "U":
            update_data(datas)

        choice = input(f"\n{MENU}\n>>>").upper()

    # Ask user did they need upload data to current file or not before program finish
    save_choice = input(f"Would you like to save to {file_name}? ").upper()
    if "N" in save_choice:
        print("Thank you for using custom-built project management software.")
    elif "Y" in save_choice:
        save_data(datas, file_name)
        print("Data save successfully"
              "\nThank you for using custom-built project management software.")


def read_file(file_name):
    """Read the file and return it as a list with use Project class"""
    datas = []
    in_file = open(file_name, "r")
    in_file.readline()
    for line in in_file:

        # replace blank character as ","
        data_part = line.strip().replace("\t", ",").split(",")
        data = Project(data_part[0], data_part[1], data_part[2], data_part[3], int(data_part[4]))
        datas.append(data)
    return datas


def save_data(datas, name):
    """Rewrite the file with current information and new information"""
    out_file = open(name, "w")

    # Add the title for file
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for data in datas:
        out_file.write(Project.string_changer(data) + "\n")


def categorical_data(datas):
    """Depends on the complete percentage to categorical datas and return it"""
    complete_project = []
    incomplete_project = []
    for data in datas:
        if Project.is_complete(data) is True:
            complete_project.append(data)
        else:
            incomplete_project.append(data)
    return complete_project, incomplete_project


def show_data(datas):
    """Classified display according to the data processed"""
    complete_project, incomplete_project = categorical_data(datas)
    print("Incomplete projects:")
    for data in incomplete_project:
        print(f"\t{data}")
    print("Completed projects:")
    for data in complete_project:
        print(f"\t{data}")


def update_data(datas):
    """Show datas, change the complete percentage of data"""
    i = 0
    for data in datas:
        print(f"{i} {data}")
        i += 1
    update_choice = int(input("Project choice: "))
    print(datas[update_choice])
    new_percentage = int(input("New Percentage: "))
    datas[update_choice].completion_percentage = new_percentage


def add_data(datas):
    """To add a new data in current project, but not save to file"""
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    completion_percentage = input("Completion percentage: ")
    data = Project(name, date, priority, cost, int(completion_percentage))
    datas.append(data)


def date_check(datas):
    """For filter data, check the date of data is greater than user input or not"""
    import datetime
    latter_project = []
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    input_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for data in datas:
        if data.date >= input_date:
            latter_project.append(data)
    return latter_project


main()
