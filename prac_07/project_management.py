"""
Project Management
Estimate: 2 hours
Actual:   2.5 hours
"""

from prac_07.project import Project
MIN_NUMBER = 0
MAX_NUMBER = 100
MAX_PRIORITY = 10
MENU_RULE = ["L", "S", "D", "F", "A", "U", "Q"]
CHOICE_RULE = ["Y", "N"]
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

    choice = get_valid_input(MENU, MENU_RULE)
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

        choice = get_valid_input(MENU, MENU_RULE)

    # Ask user did they need upload data to current file or not before program finish
    save_choice = get_valid_input(f"Would you like to save to {file_name}? (y/n)", CHOICE_RULE)
    if "N" in save_choice:
        print("Thank you for using custom-built project management software.")
    elif "Y" in save_choice:
        save_data(datas, file_name)
        print("Data save successfully"
              "\nThank you for using custom-built project management software.")


def get_valid_input(prompt, rules):
    message = input(f"{prompt}\n>>>").upper()
    while message not in (rule for rule in rules):
        print("Invalid input, Please try again.\n")
        message = input(f"{prompt}\n>>>").upper()
    return message


def get_valid_number(prompt, rule):
    number = int(input(f"{prompt}: "))
    while number > rule or number < MIN_NUMBER:
        print("Invalid number, Please try again.\n")
        number = int(input(f"{prompt}: "))
    return number


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
    update_choice = get_valid_number("Project choice", len(datas) - 1)
    print(datas[update_choice])
    new_percentage = get_valid_number("Project new percentage", MAX_NUMBER)
    datas[update_choice].completion_percentage = new_percentage


def add_data(datas):
    """To add a new data in current project, but not save to file"""
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority", MAX_PRIORITY)
    cost = get_valid_number("Cost estimate: $", 1000000.00)
    completion_percentage = get_valid_number("Completion percentage", MAX_NUMBER)
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
