from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"
def main():
    """The main program of taxi simulator."""

    # Welcome message
    print("Let's Drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill = 0
    current_taxi = None

    # Program start, get choice
    choice = input(f"{MENU}\n>>>").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":

            # If did not choice taxi, display error message.
            if current_taxi is None:
                print("You need to choose a taxi before you can drive.")
            else:
                bill += drive_taxi(current_taxi)
                print(f"Bill to date: ${bill:.2f}")
        else:

            # Error check for invalid input
            print("Invalid option")
        choice = input(f"{MENU}\n>>>").lower()

    # End message
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display available taxis and let the user choice one taxi and return it."""
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


def drive_taxi(taxi):
    """Ask the user how far to drive and calculate the trip cost and return distance"""
    try:
        distance = float(input("Drive how far? "))

        # Restart the distance
        taxi.start_fare()
        taxi.drive(distance)
        distance = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${distance:.2f}")
        return distance

    # Error check for input distance
    except ValueError:
        print("Invalid input")
        return 0


def display_taxis(taxis):
    """Display the list of taxis with their current status."""
    for i in range(len(taxis)):
        print(f"{i} - {taxis[i]}")


if __name__ == '__main__':
    main()
