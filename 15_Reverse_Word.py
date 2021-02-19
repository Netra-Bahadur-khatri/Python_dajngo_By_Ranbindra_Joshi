# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. 



def reverse_word():
    x = input("What is your name ?")
    # print(x[::-1])
    max_index = len(x) - 1
    for i in range(max_index,0,-1):
        print(x[i], end=" ")

if __name__ == "__main__":
    a = reverse_word()
    print(a)