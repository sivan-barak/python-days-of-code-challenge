#Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def count_upper_lower_cases(str):
    # initialize count
    upper_count = 0
    lower_count = 0

    # check each char if uppercase or lowercase and add to count
    for char in user_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

#request string input
print("This program will calculate the number of uppercase and lowercase letters in a given string")
user_str = input("Please enter a string: ")

#call function counting upper and lower cases in a string
upper, lower = count_upper_lower_cases(user_str)

#print outcome
print("There are {} uppercase letters and {} lowercase letters in the string".format(str(upper), str(lower)))

