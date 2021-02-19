# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function

def remove_duplicate_items_from_list():
    new_list = set()
    list1 = [1,2,3,1,4,3,2,4,5,6,7,8,9,10,6,10]
    for i in range(0,len(list1)):
        el = list1[i]
        if el in list1[i+1::]:
            new_list.add(el)

    return new_list


if __name__ == "__main__":
    x = remove_duplicate_items_from_list();
    print(x)