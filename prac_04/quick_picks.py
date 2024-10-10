"""
from random import randint
RANDOM_TIME = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
get pick_number
for row in range of 1 to pick_number
    random_picks = empty list
    while length of random_picks less than RANDOM_TIME
        random_pick = creat a random number from MIN_NUMBER to MAX_NUMBER
        if random_pick not in random_picks
            append random pick to random_picks
    sort random_picks from minimum to maximum
    display random_pick
"""
from random import randint
RANDOM_TIME = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

pick_number = int(input("How many quick picks? "))
for row in range(pick_number):
    random_picks = []
    while len(random_picks ) < RANDOM_TIME:
        random_pick = randint(MIN_NUMBER, MAX_NUMBER)  # creat random number.
        if random_pick not in random_picks:  # check repeated number.
            random_picks.append(random_pick)  # append random number to random_picks.
    random_picks.sort() # set pick in random_picks in sorted order.

    print(" ".join(f"{random_pick:2}" for random_pick in random_picks))
