def main():
    password = get_password()
    number = len(password)
    print_password(number)


def get_password():
    password = input("Enter password: ")
    while len(password) < 10:
        print("Password is too short")
        password = input("Enter password: ")
    return password


def print_password(number):
    print("*" * number)


main()
