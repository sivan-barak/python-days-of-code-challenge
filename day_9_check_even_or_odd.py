# Write a program to check if a number is even or odd.

import re
from decimal import Decimal

def check_return_number(num):
    while (re.match("^[-]?\d+(\.\d+)?$", num) is None):
        if num == "q":
            exit()
        else:
            num = input("The value entered is not a number, please try again or press 'q' to quit: ")

    #return the string converted to number
    if (re.match(".*\..*", num) is None):
        return int(num)
    else:
        return Decimal(num)

def is_even(num):
    # check if integer or decimal
    if (isinstance(num, int)):
        # if integer, check if whole number is divisible by 2
        if (num % 2 == 0):
            return True
        else:
            return False
    else:
        # if decimal, check if last nonzero digit after decimal point is divisible by 2
        last_deci_digit = int(str(num).rstrip("0")[-1])
        if (last_deci_digit % 2 == 0):
            return True
        else:
            return False



print("This program will check if a number is even or odd")

# number as input
user_num = check_return_number(input("Enter number: "))

# check number is if even or odd
even = is_even(user_num)

# output result
print("The number is", "even" if even else "odd")
