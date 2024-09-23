"""
function main
    password = get_password()
    number = len of password
    print_password(number)
function get_password
    get password
    while len of password less than 10
        display the password is too short
        get password
    return password
function print_password
    display "*" multiply by number
"""
def main():
    password = get_password()
    number = len(password)
    print_password(number)


def get_password():
    """This function for get the password and check it valid or not"""
    password = input("Enter password: ")
    while len(password) < 10:
        print("Password is too short")
        password = input("Enter password: ")
    return password


def print_password(number):
    """This function for print "*" via the length of the password"""
    print("*" * number)


main()
