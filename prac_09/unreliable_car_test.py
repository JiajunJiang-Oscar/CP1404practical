from prac_09.unreliable_car import UnreliableCar
from random import randint

def main():
    """Test for unreliable car class."""
    car = UnreliableCar("Toyota", 100)

    # Call the method drive and offer the distance as a random number
    car.drive(randint(0, 100))

    # Display the message
    print(f"{car}")

if __name__ == '__main__':
    main()
