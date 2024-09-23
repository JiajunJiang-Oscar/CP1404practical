"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

pseudocode:
HIGH_BONUS_RATE equal to 0.15
LOW_BONUS_RATE equal to 0.1
get sales
while sales great and equal to 0
    if sales great and equal to 1000
        bonus = sales * HIGH_BONUS_RATE
        display bonus
        get sales
    else if sales less than 1000
        bonus = sales * LOW_BONUS_RATE
        display bonus
        get sales
"""

HIGH_BONUS_RATE = 0.15
LOW_BONUS_RATE = 0.1
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * HIGH_BONUS_RATE
        print(f"Your bonus is: {bonus:.2f}")
        sales = float(input("Enter sales: $"))
    elif sales < 1000:
        bonus = sales * LOW_BONUS_RATE
        print(f"Your bonus is: {bonus:.2f}")
        sales = float(input("Enter sales: $"))
