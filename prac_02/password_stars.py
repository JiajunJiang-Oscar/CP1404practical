"""
function main
    password = get_password()
    number = len of password
    star_number = print_password
    display star_number
function get_password
    get password
    while len of password less than 10
        display the password is too short
        get password
    return password
function print_password
    return "*" multiply by number
"""


def main():
    password = get_password()
    number = len(password)
    star_number = print_password(number)
    print(star_number)


def get_password():
    """This function for get the password and check it valid or not"""
    password = input("Enter password: ")
    while len(password) < 10:
        print("Password is too short")
        password = input("Enter password: ")
    return password


def print_password(number):
    """This function for print "*" via the length of the password"""
    return "*" * number


main()
