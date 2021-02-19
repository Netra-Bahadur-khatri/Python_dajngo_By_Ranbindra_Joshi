# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

#  Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

def guess_random_one():
    print("Guess any number.")
    a = random.randint(1,10)
    if a >= 10 and a <= 20:
        print("Your guess is too high.")
    elif a <= 0:
        print("Your guess is too low.")
    elif a == 5:
        print("Your is exactly correct.")
    else:
        print("Invalid input")

if __name__ == "__main__":
    x = guess_random_one()
    print(x)