# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.



a = [1,4,9,16,25,36,49,64,81,100]
# b = [x for x in a if x % 2 == 0]
def print_even_elements_from_list():
    b = []
    for x in a:
        if x % 2 == 0:
            b.append(x)
    return b


if __name__ == "__main__":
    c = print_even_elements_from_list()
    print(c)