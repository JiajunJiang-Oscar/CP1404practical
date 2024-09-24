"""
menu = (G)et a valid score, (P)rint result, (S)how stars, (Q)uit
function main
    score equal to 0
    display menu
    get choice
    while choice is not equal to "Q"
        if choice is equal to "G"
            score = get_valid_score
            display score, menu
            get choice
        else if choice is equal to "P"
            result = determine_grade
            print result, menu
            get choice
        else if choice is equal to "S"
            stars = print_stars
            display stars, menu
            get choice
        else
            display error message, menu
            get choice
    display farewell message
def get_valid_score
    get number
    while number less than 0 or number great than 100:
        display error message
        get number
    return number
def determine_grade
    if score great or equal to 90:
        grade = "Excellent"
    else if score less than 90 and score great or equal to 50:
        grade = "Passable"
    else
        grade = "Bad"
    return grade
def print_stars
    return "*" * score
"""


MENU = ("(G)et a valid score"
        "\n(P)rint result"
        "\n(S)how stars "
        "\n(Q)uit")
def main():
    score = 0
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(f"Your score is {score}")
            print(MENU)
            choice = input(">>>").upper()
        elif choice == "P":
            result = determine_grade(score)
            print(result)
            print(MENU)
            choice = input(">>>").upper()
        elif choice == "S":
            stars = print_stars(score)
            print(stars)
            print(MENU)
            choice = input(">>>").upper()
        else:
            print("Invalid choice")
            print(MENU)
            choice = input(">>>").upper()
    print("Farewell!")


def get_valid_score():
    """This function for getting the score and check it valid or not."""
    number = int(input("Please enter your score:"))
    while number < 0 or number > 100:
        print("Score must be between 0 and 100")
        number = int(input("Please enter your score:"))
    return number


def determine_grade(score):
    """This function for use the score to determine the grade."""
    if score >= 90:
        grade = "Excellent"
    elif 90 > score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


def print_stars(score):
    """This function for printing the stars via the score."""
    return "*" * score


main()
