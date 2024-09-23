"""
function main
    MENU = ("C - Convert Celsius to Fahrenheit"
            "\nF - Convert Fahrenheit to Celsius"
            "\nQ - Quit")
    display MENU
    get choice in upper case
    while choice != to Q
        if choice == C
            fahrenheit = celsius_to_fahrenheit()
            display Fahrenheit
        else if choice == F
            celsius = fahrenheit_to_celsius()
            display Celsius
        else
            display error message
        display MENU
        get choice in upper case
    display finish message
function celsius_to_fahrenheit
    get Celsius
    calculater Celsius to Fahrenheit
    return Celsius
function fahrenheit_to_celsius
    get Fahrenheit
    calculater Fahrenheit to Celsius
    return Fahrenheit
"""
def main():
    MENU = ("C - Convert Celsius to Fahrenheit"
            "\nF - Convert Fahrenheit to Celsius"
            "\nQ - Quit")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = celsius_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = fahrenheit_to_celsius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")



def celsius_to_fahrenheit():
    """This function for converting Celsius to Fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius():
    """This function for converting Fahrenheit to Celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * fahrenheit - 32
    return celsius


main()
