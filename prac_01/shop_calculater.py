"""
total_price equal to 0
get item_number
for i in range from 1 to item_number + 1
    get item_price
    while item_price equal to 0
        display error message
        get item_price
    total_price = total_price + item_price
display total_price and item_number
"""

total_price = 0
item_number = int(input("Number of items: "))
for i in range(item_number):
    item_price = float(input("Price of item: "))
    while item_price <= 0:
        print("Invalid number of items!")
        item_price = float(input("Price of item: "))
    total_price += item_price
print(f"Total price for {item_number} items is ${total_price}")
