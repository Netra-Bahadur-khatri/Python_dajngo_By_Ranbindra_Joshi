# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

#  Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

def password_generator(strength = 0):
    pass_length = random.randint(8, int((8 + strength) * 1.5))
    password = ''
    while pass_length > 0:
        pass_length -= 1
        pass_char = random.choice(['a','b','$','7','@', '_'])
        password += pass_char
    return password

if __name__ == "__main__":
    a = password_generator()
    print(a)