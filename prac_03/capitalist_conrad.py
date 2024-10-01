"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)

import random
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
MAX_INITIAL_PRICE = 100
MIN_INITIAL_PRICE = 1
number_of_days = 0
price = creat random number from MIN_INITIAL_PRICE to MAX_INITIAL_PRICE
open capitalist.txt as out_file to write
display starting price in out_file
while MIN_PRICE less or equal to price or price less and equal to MAX_PRICE
    price_change = 0
    if random number(1, 2) == 1:
        price_change = random uniform from 0 to MAX_INCREASE
    else
        price_change = random uniform from -MAX_DECREASE to 0
    number_of_days = number_of_days + 1
    price = price * (1 + price_change)
    display number_of_days, price with two decimal in out_file
out_file close
display finish message
"""

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
MAX_INITIAL_PRICE = 100
MIN_INITIAL_PRICE = 1
FILENAME = "capitalist.txt"


price = random.randint(MIN_INITIAL_PRICE, MAX_INITIAL_PRICE)
out_file = open(FILENAME, 'w')
print(f"Starting price: ${price:,.2f}", file=out_file)
number_of_days = 0

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases

    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)

    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    number_of_days += 1
    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()
print("Output print: Done")
