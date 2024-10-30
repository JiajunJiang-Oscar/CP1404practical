from prac_06.guitar import Guitar

guitars = [
    Guitar("Gibson L-5 CES", 1924, "$16,035.40"),
    Guitar("Another Guitar", 2015, "$  1,512.90")
]
name = input("Name: ")
while name != "":
    year = input("Year: ")
    cost = input("Cost: ")
    guitars.append(Guitar(name, int(year), cost))
    print(f"{name} ({year}) : {cost} added.\n")

    name = input("Name: ")
print("\n... snip ...\n"
      "\nThere are my guitars:")
for guitar in guitars:
    if guitar.is_vintage():
        message = "(vintage)"
    else:
        message = ""
    print(guitar, message)

