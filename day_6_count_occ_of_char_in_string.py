#Write a program to count the occurrences of a specific character in a string.

print("This program will count the occurrences of a specific character in a string")
mystr = input("Please enter a string: ")
mychar = input("Please enter a character: ")
count_of_chars = mystr.count(mychar)
if count_of_chars == 1:
    print('The string "{}" has 1 character'.format(mystr))
else:
    print('The string "{}" has {} characters'.format(mystr, count_of_chars))
