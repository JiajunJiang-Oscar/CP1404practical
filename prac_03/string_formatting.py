"""
This code is for display the information in correct format
name = "Gibson L-5 CES"
year = 1922
cost = 16035.9
display year, name and cost in correct format
"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

print(f"{year} {name} for about ${cost:,.0f}!")


"""
This code is for display a chart start with 2 ^ 0 end with 2 ^ 10
for i in range start with 0 end with 10
    result equal to 2 ** i
    display result
"""
for i in range(0, 11):
    result = 2 ** i
    print(f"2 ^ {i:>2} is {result:>5}")
