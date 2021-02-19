# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)



# list = [2,4,5,6,7,8,9]
def divisior():
    new_List = []
    x = int(input("Enter a number for divisible: "))
    for a in range(1,x):
        # new_List.append(a)
        if x % a == 0:
            new_List.append(a)
    
    return new_List

if __name__ == "__main__":
    print(divisior())
