"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia",
    "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
display dictionary
get user input in uppercase
while user input not equal to empty
    if user input in CODE_TO_NAME
        display state name
    else
        display invalid message
    get user input in uppercase
"""

# This dictionary shows the Australian state abbreviations and names.
# The user will enter the state abbreviations and get full name.
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT" : "Northern Territory",
    "WA" : "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()

# Keep asking the state abbreviations till the user enter empty message.
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")

    state_code = input("Enter short state: ")
