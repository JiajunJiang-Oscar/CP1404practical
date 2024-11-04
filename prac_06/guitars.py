"""
Guitars
Estimate: 20 minutes
Actual:   27 minutes

import Guitar from guitar in prac_06
guitars = [
    in Guitar name = "Gibson L-5 CES", year = 1924, price = "16,035.40",
    in Guitar name = "Another Guitar", year = 2015, price = "1,512.90"
]
get name
while name not equal to empty
    get year, cost
    append name, year in integer, cost in guitars
    display added message
    get name
display snip message
for i, guitar in enumerate guitars
    if guitar call method is_vintage equal to True
        message = "(vintage)"
    else
        message = empty
    display information in class in correct format
"""

from prac_06.guitar import Guitar

def main():
    """This program to get guitar information and display it"""
    guitars = []

    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")
        guitars.append(Guitar(name, int(year), cost))

        # add success message
        print(f"{name} ({year}) : {cost} added.\n")

        # get input again
        name = input("Name: ")

    # Add the two default information in list when input is finish
    guitars.append(Guitar("Gibson L-5 CES", 1924, "16,035.40"))
    guitars.append(Guitar("Another Guitar", 2015, "1,512.90"))

    # Print the halving line
    print("\n... snip ...\n"
          "\nThere are my guitars:")

    for i, guitar in enumerate(guitars, 1):
        # Check the return value and add message
        if guitar.is_vintage():
            message = "(vintage)"
        else:
            message = ""

        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:>10}{message}")

main()
