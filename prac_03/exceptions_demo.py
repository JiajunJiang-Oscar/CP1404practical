"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Answer:
1. When the user inputs are not the integer, example: 'asdfghjkl' or '123.12'
2. When the user input of denominator is 0 (The denominator can not be 0)
3. Delete the except ZeroDivisionError and add an error check program.
    (I write the code which is after changed under the original code as a comment)
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# # Answer for question 3:
# try:
#     numerator = int(input("Enter the numerator:"))
#     denominator = int(input("Enter the denominator: "))
#     if denominator == 0:
#         print("The denominator cannot be 0")
#         denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
#
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
#
# print("Finished.")
