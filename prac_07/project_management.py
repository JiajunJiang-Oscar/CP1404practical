"""
Project Management
Estimate: 120 minutes
Actual:   minutes
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

    choice = input(f"{MENU}\n>>>").upper()
    while choice != "Q":
        if choice == "L":
            new_file_name = input("Please enter file name\n>>>")
            datas = read_file(new_file_name)

        elif choice == "S":
            print(f"The current file name is {file_name}")
            out_file = open(file_name, "w")
            out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for data in datas:
                out_file.write(Project.string_changer(data) + "\n")
            print("Data save successfully")

        elif choice == "D":
            write_file(datas)

        elif choice == "F":
            latter_project = data_check(datas)
            for data in latter_project:
                print(data)

        elif choice == "A":
            print("Let's add a new project")
            add_data(datas)

        elif choice == "U":
            update_data(datas)

        choice = input(f"\n{MENU}\n>>>").upper()
    print("Farewell")


def write_file(datas):
    complete_project, incomplete_project = categorical_data(datas)
    print("Incomplete projects:")
    for data in incomplete_project:
        print(f"\t{data}")
    print("Completed projects:")
    for data in complete_project:
        print(f"\t{data}")


def update_data(datas):
    i = 0
    for data in datas:
        print(f"{i} {data}")
        i += 1
    update_choice = int(input("Project choice: "))
    print(datas[update_choice])
    new_percentage = int(input("New Percentage: "))
    datas[update_choice].completion_percentage = new_percentage


def add_data(datas):
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    completion_percentage = input("Completion percentage: ")
    data = Project(name, date, priority, cost, int(completion_percentage))
    datas.append(data)


def data_check(datas):
    import datetime
    latter_project = []
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date().strftime("%d/%m/%Y")
    for data in datas:
        if data.date >= date:
            latter_project.append(data)
    return latter_project


def categorical_data(datas):
    complete_project = []
    incomplete_project = []
    for data in datas:
        if Project.is_complete(data) is True:
            complete_project.append(data)
        else:
            incomplete_project.append(data)
    return complete_project, incomplete_project


def read_file(file_name):
    datas = []
    in_file = open(file_name, "r")
    in_file.readline()
    for line in in_file:
        data_part = line.strip().replace("\t", ",").split(",")
        data = Project(data_part[0], data_part[1], data_part[2], data_part[3], int(data_part[4]))
        datas.append(data)
    return datas


main()
