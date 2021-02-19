# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


# Program to check either number is even or odd.
num = int(input("Enter a number : "))
def odd_Even():
    if(num % 2 == 0):
        print("Even Number.")
    else:
        print("Odd Number. ")

if __name__ == "__main__":
    odd_Even()


# Program to check whether the number is exactly divisible by 4 or not.
check_num = int(input("Enter a number to check multiple of four: "))
def check_multiple_of_four():
    if(check_num / 4 == 0 ):
        print("The number is exactly divisible of four.")
    elif (check_num / 2 == 0):
        print("Divisible by subsets of four not exactly four.")
    else:
        print("The number is not divisible by four.")

if __name__ == "__main__":
    check_multiple_of_four()