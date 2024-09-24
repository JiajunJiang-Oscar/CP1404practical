"""
import random
function main
    score = get_valid_score
    grade = determine_grade
    display grade
    random_score = creat a random number from 0 to 100
    random_grade = determine_grade
    display random_score, random_grade
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
    """This function for get score and check it is valid or not."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_grade(number):
    """This function for determine the grade in different condition."""
    if number >= 90:
        grade = "Excellent"
    elif 90 > number >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


main()
