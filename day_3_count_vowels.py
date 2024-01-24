#Write a function to count the number of vowels in a given string.

def count_vowels(s):
    s = s.lower()
    count = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")
    return count

print("This program will count the number of vowels in a given string")
mystr = input("Please enter a string: ")
amt_of_vowels = count_vowels(mystr)
if amt_of_vowels == 1:
    print('The string "{}" has 1 vowel'.format(mystr))
else:
    print('The string "{}" has {} vowels'.format(mystr, amt_of_vowels))
