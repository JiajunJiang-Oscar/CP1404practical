"""
Project Management
Estimate: 2 hours
Actual:   3 hours

!!! Pseudocode, actual code start with Line 99 !!!
import datetime
import Project from project
constant group...
function main
    file name = projects.txt
    call read_file with file name and save as data
    display welcome message
    call get_valid_input with MENU and save as choice
    while choice not equal to "Q"
        if choice equal to "L"
            get name of new file
            call read_file with new file name and save as data
        else if choice equal to "S"
            get name of save file
            call save_data with save file name
            display success message
        else if choice equal to "D"
            call show_data with datas
        else if choice equal to "F"
            call date_check with datas and save as latter project
            display data in latter project
        else if choice equal to "A"
            display start message
            call add_data with datas
        else if choice equal to "U"
            call update_data with datas
        call get_valid_input with MENU and save as choice
    call get_valid_input with save message and save as save_choice
    if "N" in save_choice
        display end message
    else if "Y" in save_choice
        call save_data with save file name and save data
        display end message
function get_valid_input
    display prompt and get message
    while message not in rules
        display error message, prompt and get message
    return message
function get_valid_number(prompt, rules)
    display prompt and get number
    while number > rules or number < 0
        display error message, prompt and get message
    return message
function read_file
    datas = empty list
    open file_name and read, save as data
    skip first line
    for line in in_file
        replace blank as ",", strip space and split with "," and save as data_part
        data = Project(data_part[0], data_part[1], data_part[2], data_part[3], int(data_part[4]))
        append data to datas
    return datas
function save_data
    out_file = open file with name and write
    add first line for file
    for data in datas
        write data to out_file
function categorical_data
    complete_project, incomplete_project = empty list
    for data in datas
        if Project.is_complete return True
            append data to complete_project
        else
            append data to complete_project
    return complete_project, incomplete_project
function show_data
    complete_project, incomplete_project = categorical_data
    for data in incomplete_project, complete_project
        display incomplete data, complete data
function update_data
    i = 0
    for data in datas
        display i, data
        i += 1
    call get_valid_input with Project choice, limited by (length of datas - 1) and save as update_choice
    display current updated data
    call get_valid_number and get new percentage
    change the percentage of updated data to current percentage
function date_check
    latter_project = empty list
    get date_string in datetime format
    for data in datas
        if data.date great or equal to input_date
            append data to latter_project
    return latter_project
def add_data
    get name, date, priority, cost, percentage,
    data = Project(name, date, priority, cost, percentage)
    append data to datas
"""


import datetime
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
    """Call all functions when needed, display the message return from functions and menu when program start"""

    # Default file name
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
    """Check the input is valid or not by rules"""
    message = input(f"{prompt}\n>>>").upper()

    while message not in (rule for rule in rules):
        print("Invalid input, Please try again.\n")
        message = input(f"{prompt}\n>>>").upper()
    return message


def get_valid_number(prompt, rule):
    """Check the number input is valid or not by rules"""
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


def date_check(datas):
    """For filter data, check the date of data is greater than user input or not"""
    # import datetime
    latter_project = []
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    input_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    for data in datas:
        if data.date >= input_date:
            latter_project.append(data)
    return latter_project


def add_data(datas):
    """To add a new data in current project, but not save to file"""
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority", MAX_PRIORITY)
    cost = get_valid_number("Cost estimate: $", 1000000.00)
    completion_percentage = get_valid_number("Completion percentage", MAX_NUMBER)
    data = Project(name, date, priority, cost, int(completion_percentage))
    datas.append(data)


main()
