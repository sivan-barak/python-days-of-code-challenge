#Write a program to check if a number is positive, negative, or zero.
import re

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


print("This program will check if a number is positive, negative, or zero")

# number as input
n = check_and_return_number(input("Enter number: "))

print("The number is", end=" ")
if (n>0):
    print("positive")
elif (n<0):
    print("negative")
else:
    print("zero")