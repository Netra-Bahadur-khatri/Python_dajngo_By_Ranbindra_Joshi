# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
# age = 12

import datetime
def user_age():
    # global age
    age =  int(input("Enter user age: \n"))
    return age

def PersonDetails():

    now = datetime.datetime.now()
    year = now.year
    age = user_age()
    to_100 = year + 100 - age
    print('You will be 100 years old in ', to_100,' years')


if __name__ == "__main__":
    PersonDetails()


