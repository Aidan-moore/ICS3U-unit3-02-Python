#!/usr/bin/env python3

# Created by: Aidan Moore
# Created on: Sept 2021
# number game
# Import the random module
import random

# Computer chooses a random number between 1 and 1000
target = random.randint(1, 9)

retries = 0

while True:

    # Taking user choice
    choice = int(input("Enter your choice: "))
    retries += 1

    # Wrong guess
    if target != choice:

        print("Wrong Guess!! Try Again A-")

        # Hint
        if target < choice:
            print("The required number lies between 0 and {}".format(choice))
        else:
            print("The required number lies between {} and 9".format(choice))

    # Correct choice
    else:
        print("You guessed the correct number after {} retries A+".format(retries))
        # User guessed the correct value
        # So let's end the infinite loop
        break
