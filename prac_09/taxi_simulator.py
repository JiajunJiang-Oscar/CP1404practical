from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's Drive!")
    choice = input(f"{MENU}\n>>>").lower()
    while choice != "q":
        if choice == "c":
            print("c")
        elif choice == "d":
            print("d")
        else:
            print("Invalid option")
        choice = input(f"{MENU}\n>>>").lower()
    print("Bye")

if __name__ == '__main__':
    main()
