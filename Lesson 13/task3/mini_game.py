import random


def roll_three_dice():
    rolls = []
    for x in range(3):
        random_int = random.randint(1, 6)
        print(random_int)
        rolls.append(random_int)

    if 5 in rolls:
        print("You lost")
    else:
        print("You won")
