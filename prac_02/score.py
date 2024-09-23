"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint
def main():
    score = get_valid_score()
    grade = determine_grade(score)
    print(grade)
    random_score = randint(0, 100)
    random_grade = determine_grade(random_score)
    print(f"The random score is {random_score} and grade is {random_grade}")


def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_grade(number):
    if number >= 90:
        grade = "Excellent"
    elif 90 > number >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


main()
