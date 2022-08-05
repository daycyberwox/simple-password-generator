#!/usr//bin/python3
# A very simple password generator script

import string  # module to create your own strings
import random  # module to generate random numbers

print("*" * 45)
print('Welcome to The Simple Password Generator!')
print("*" * 45)
print('\n')



characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    length = int(input("Enter desired password length: "))  # user's desired length of password
    random.shuffle(characters)                                       # shuffling the character
    password = []                                           
    
    for i in range(length):                                          # picking random characters from the list
        password.append(random.choice(characters))

    random.shuffle(password)                                         # shuffling the password
    print("".join(password))                                         # converting the list to a string and removing the spaces ""

generate_password()                                                  # invoking the function
