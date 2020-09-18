# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right.

import random as r
a = r.randint(1, 9)

def ask_user():
    u = int(input("Guess the number?\n"))

    if a == u:
        print("Exactly")
    elif a > u:
        print("Too low")
        ask_user()
    else:
        print("Too high")
        ask_user()

ask_user()
