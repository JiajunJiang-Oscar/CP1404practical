"""
HEX_TO_COLOUR = {"Purple": "#a020f0", "Amber": "#ffbf00", "Red": "#ff0000", "Tiffany": "#0abab5", "Yellow": "#ffff00",
                 "White": "ffffff", "Plum": "#8e4585", "Peach": "ffe5b4", "Olive": "#808000", "Melon": "#febaad"}
get user input in title case
while input not equal to empty
    try
        display the colour name, hex code
    except KeyError
        display error message
    get user input in title case
display end message
"""
HEX_TO_COLOUR = {"Purple": "#a020f0",
                 "Amber": "#ffbf00",
                 "Red": "#ff0000",
                "Tiffany": "#0abab5",
                 "Yellow": "#ffff00",
                 "White": "ffffff",
                 "Plum": "#8e4585",
                 "Peach": "ffe5b4",
                 "Olive": "#808000",
                 "Melon": "#febaad"
                 }

hex_code = str(input("Enter the name of the colour to get hex code >>>").title())

while hex_code != "":
    try:
        print(f"{hex_code:7} is {HEX_TO_COLOUR[hex_code]}")

    except KeyError:
        print("Invalid input")
    hex_code = str(input("Enter short state: ").title())

print("Farewell")
