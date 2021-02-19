# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def palindrome_check_string():
    x = input("Enter an string as you want: \n")
    if x[::] == x[::-1]:
        print("Given string is palindrome.")
    else:
        print( "Given string is not palindrome.")

if __name__ == "__main__":
    palindrome_check_string()




