#Write a program to find the maximum and minimum values in a list.

import re

def check_and_return_non_negative_integer(num):
    while (not num.isdigit()):
        if num == "q":
            exit()
        else:
            num = input("The value entered is not a positive number, please try again or press 'q' to quit: ")
    return int(num)

def check_and_return_number(num):
    while (re.match("[-]?\d+(\.\d+)?", num) is None):
        if num == "q":
            exit()
        else:
            num = input("The value entered is not a number, please try again or press 'q' to quit: ")

    #return the string converted to number
    if (re.match(".*\..*", num) is None):
        return int(num)
    else:
        return float(num)


print("This program will find the maximum and minimum values in a list")

# creating an empty list
lst = []

# number of elements as input
n = check_and_return_non_negative_integer(
    input("Enter number of elements or 'q' to quit: "))

# iterating for the amount of elements
for i in range(0, int(n)):
    ele = check_and_return_number(input("Enter an element: "))
    # adding the element to the list
    lst.append(ele)

print("The minimum and maximum of list:", lst, "are ",min(lst), max(lst))
