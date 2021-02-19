# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.


# Python program to checks an prime numbers 

def checks_prime_number():
    x = list(map(int,input("\nEnter an number: ").split()))
    print("The list of number is: ",x)
    print("\n")
    new_list = []
    print("Returning an list of prime numbers: ")
    for a in x:
        if a % 2 != 0:
            new_list.append(a)
    return new_list

if __name__ == "__main__":
    a = checks_prime_number()
    print(a)










