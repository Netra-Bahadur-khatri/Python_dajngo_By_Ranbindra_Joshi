# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


def return_common_elements_bet_list(x,y):
    new_list = []
    for a in x:
        if a in y:
            new_list.append(a)
    return new_list

if __name__ == "__main__":
    list1 = [1,1,2,3,5,8,13,21,34,55,89]
    list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    c = return_common_elements_bet_list(list1, list2)
    print(c)











