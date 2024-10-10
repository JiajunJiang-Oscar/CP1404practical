"""
CP1404/CP5632 Practical
Data file -> lists program

FILENAME = "subject_data.txt"
function main
    call the load_data function and save the information as a list
    call the print_data function to print the data
function load_data
    input file = open the FILENAME
    set the lists as an empty list
    for line in input file
        line = line strip the NUL
        parts = line information split with ','
        append the parts into lists
    close the input file
    return lists
function print_data
    display the halving line
    for i in range from 1 to the length of data + 1
        display class code, lecture name and students number
"""


FILENAME = "subject_data.txt"
def main():
    """This function is for call the load data function and print data function."""
    data = load_data()
    print_data(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    lists = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        lists.append(parts)
    input_file.close()
    return lists


def print_data(data):
    """This function is for display the data and halving line."""
    print("----------")  # print the halving line
    for i in range(1, len(data) + 1):
        print(f"{data[i - 1][0]} is taught by {data[i - 1][1]:<12} and has {data[i - 1][2]:>3} students.")


main()
