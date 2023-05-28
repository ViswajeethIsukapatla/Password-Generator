# Password Generator

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&/*")

def generate_password():
    password_length = int(input("Length Of The Password:"))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)

    print(password)

option = input("Input (Yes/No) To Generate Password:")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Quitting")
    quit()
else:
    print("Invalid Input, Please Enter Yes or No")
    quit()     
