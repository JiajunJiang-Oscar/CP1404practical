import random

print(random.randint(5, 20))
# I see a random number from 5 to 20.
# The minimum I can see is 5， maximum is 20.
print(random.randrange(3, 10, 2))
# Line 2 can use in line 4 but need to set the step as 1.
# The minimum I can see is 3， maximum is 9.
print(random.uniform(2.5, 5.5))
# I see a floating-point number from 2.5 to 5.5 and the number of decimal places is not fixed.
# The minimum I can see is 2.5， maximum is 5.5.
print(random.randint(1, 100))
