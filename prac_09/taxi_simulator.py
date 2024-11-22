from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's Drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill = 0
    current_taxi = None
    choice = input(f"{MENU}\n>>>").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            print("d")
        else:
            print("Invalid option")
        choice = input(f"{MENU}\n>>>").lower()
    print("Bye")


def choose_taxi(taxis):
    """Display available taxis and allow the user to select one."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


def display_taxis(taxis):
    """Display the list of taxis with their current status."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == '__main__':
    main()
