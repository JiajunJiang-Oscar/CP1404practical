"""
Project Management
Estimate: minutes
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
    datas = read_file()

    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            print("L")
        elif choice == "S":
            print("S")
        elif choice == "D":
            print("D")
            for data in datas:
                print(data)
        elif choice == "F":
            print("F")
        elif choice == "A":
            print("A")
        elif choice == "U":
            print("U")
        choice = input(">>>").upper()
    print("Q")


def read_file():
    datas = []
    in_file = open("projects.txt", "r")
    in_file.readline()
    for line in in_file:
        data_part = line.strip().replace("\t", ",").split(",")
        data = Project(data_part[0], data_part[1], data_part[2], data_part[3], data_part[4])
        datas.append(data)
    return datas


main()
