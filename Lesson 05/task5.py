import random

rnd_number = random.randint(1, 10)

user_guess = int(input("Guess the secret number from 1 to 10: "))

if rnd_number == user_guess:
    print(f"Correct! Secret number is {rnd_number}")
else:
    print(f"Sorry, you missed. Secret number is {rnd_number}")
