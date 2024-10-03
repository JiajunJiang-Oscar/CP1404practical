# question 1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# question 2
in_file = open("name.txt", "r")
name = in_file.readline()
in_file.close()
print(f"Hi! {name}")

# question 3
file_name = "numbers.txt"
with open(file_name, "r") as file:
    line1 = file.readline()
    line2 = file.readline()

    total = int(line1) + int(line2)
    print(total)

# question 4
file_name = "numbers.txt"
with open(file_name, "r") as file:
    total_number = 0
    for line in file:
        total_number += int(line)
    print(total_number)