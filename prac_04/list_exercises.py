"""
NUMBER_OF_NUMBERS = 5
set numbers as an empty lest
for i in range NUMBER_OF_NUMBERS
    get number
    append number to numbers
average_number = the sum of all numbers / NUMBER_OF_NUMBERS
display first number in list, last number in list, smallest number in list and largest number in list
display average number in list
"""

NUMBER_OF_NUMBERS = 5
numbers = []

for i in range(NUMBER_OF_NUMBERS):
    number = int(input(f"Enter the number {i + 1} >>> "))
    numbers.append(number)

average_number = sum(numbers) / NUMBER_OF_NUMBERS

print(f"The first number is {numbers[0]}"
      f"\nThe last number is {numbers[-1]}"
      f"\nThe smallest number is {min(numbers)}"
      f"\nThe largest number is {max(numbers)}"
      f"\nThe average number is {average_number:.1f}")
