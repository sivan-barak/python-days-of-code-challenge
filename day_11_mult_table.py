#Write a program to print the multiplication table of a given number.

import re
from decimal import Decimal

def check_return_number(num):
    while (re.match("^[-]?\d+(\.\d+)?$", num) is None):
        if num == "q":
            exit()
        else:
            num = input("The value entered is not a number, please try again or press 'q' to quit: ")

    #return the string converted to a number
    if (re.match(".*\..*", num) is None):
        return int(num)
    else:
        return Decimal(num)

def print_multiplication_table_for_integer(num):
    for i in range(1,13):
        print(f"{i} * {num} = {i*num}")


print("This program will print the multiplication table from 1 to 12 of a given number")

# get a number from the user
n = check_return_number(
    input("Enter a number or 'q' to quit: "))

print_multiplication_table_for_integer(n)
