# Version 1.0
# 02/21/2021
# Created by: Colton Simms

import string
from random import *

print("Welcome to the Simple Python Password Generator!\n")
print("Passwords must be a minimum of 6 characters long.")

pwLength = 0
while pwLength < 6:
    pwLength = int(input("Enter how long you want the password to be: "))
    if pwLength >= 6:
        continue

lengthCheck = False
while not lengthCheck:
    pwLettersLength = int(input("Enter how many letters you want in the password: "))
    pwNumbersLength = int(input("Enter how many numbers you want in the password: "))
    if (pwLettersLength + pwNumbersLength) > pwLength or (pwLettersLength + pwNumbersLength) < pwLength:
        print("The password length is " + str(pwLength) + ". \nPlease try again!")
    else:
        lengthCheck = True
password = ""
for x in range(pwLettersLength):
    password += "".join(choice(string.ascii_letters))
for x in range(pwNumbersLength - 1):
    password += "".join(str(randint(0, 10)))

scrambled_password = ''.join(sample(password, len(password)))
print(scrambled_password)
