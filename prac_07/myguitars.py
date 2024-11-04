import csv
from prac_07.guitar import Guitar

def main():
    """Read file of guitar, save as objects, ask for new guitar, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')

    for line in in_file:
        line = line.strip().split(",")
        guitar = Guitar(line[0], int(line[1]), line[2])
        guitars.append(guitar)
    in_file.close()

    # Ask for get new guitar input and write in csv
    add_message = []
    name = input("Name: ")

    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")
        add_message.append([name, year, cost])

        # write information to csv here
        with open("guitars.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(add_message)

        # display add success message
        print(f"{name} ({year}) : {cost} added.\n")

        # get input again
        name = input("Name: ")

    # sort for guitars list
    guitars.sort()

    # display the halving line and information in csv
    print("\n... snip ...\n")
    for guitar in guitars:
        print(guitar)

main()
