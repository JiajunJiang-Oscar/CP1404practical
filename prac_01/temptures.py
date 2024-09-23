"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

MENU = ("C - Convert Celsius to Fahrenheit"
        "\nF - Convert Fahrenheit to Celsius"
        "\nQ - Quit")
display MENU
get choice in upper case
while choice != to Q
    if choice == C
        get Celsius
        calculate Fahrenheit
        display Fahrenheit
    else if choice == F
        get Fahrenheit
        calculate Celsius
        display Celsius
    else
        display error message
    display MENU
    get choice in upper case
display finish message
"""

MENU = ("C - Convert Celsius to Fahrenheit"
        "\nF - Convert Fahrenheit to Celsius"
        "\nQ - Quit")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * fahrenheit - 32
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
