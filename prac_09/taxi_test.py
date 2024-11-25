from prac_09.taxi import Taxi

def main():
    """Test for taxi class."""
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km, display the taxi's details, current fare
    my_taxi.drive(40)
    print(f"{my_taxi}, Current Fare:{my_taxi.get_fare()}")

    # Restart the meter and then drive the car 100 km, display details, current fare
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, Current Fare:{my_taxi.get_fare()}")

main()