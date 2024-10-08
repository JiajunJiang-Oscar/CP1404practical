"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """This function will get the month number and pre month incomes."""
    incomes = []
    month_number = int(input("How many months? "))

    for month in range(1, month_number + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print_report(incomes, month_number)


def print_report(incomes, month_number):
    """This function will display the report via given month number and incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_number + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
