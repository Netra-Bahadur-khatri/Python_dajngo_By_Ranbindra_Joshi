
# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

# Program to print out all the elements that are less than five.
list_1 = [10,5,6,2,3,1,9]
def less_than_five_InList():
    flag = True
    for a in list_1:
        if a <= 5:
            print(a)
            flag = False

    if flag:
        print("No elements in the list are less than five.")


# Program to return all the elements that are less than 5 in certain list.
def return_list_of_less_than_five(input_list):
    less_than_five = []
    for b in input_list:
        if b <= 5:
            less_than_five.append(b)
    return less_than_five        

if __name__ == "__main__":
    less_than_five_InList()
    new_list1 = [12,13,24,0,45,67,78,1,2,3,4]
    x = return_list_of_less_than_five(new_list1)
    print(x)
