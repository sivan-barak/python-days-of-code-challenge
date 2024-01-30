#Write a program to remove duplicates from a list.


def check_and_return_non_negative_integer(num):
    while (not num.isdigit()):
        if num == "q":
            exit()
        else:
            num = input("The value entered is not a non-negative number, please try again or press 'q' to quit: ")
    return int(num)



print("This program will remove duplicates from a list")

# creating an empty list
lst = []

# number of elements as input
n = check_and_return_non_negative_integer(
    input("Enter number of elements or 'q' to quit: "))

# iterating till the range
for i in range(0, int(n)):
    ele = input("Enter an element: ")
    # adding the element to the list
    lst.append(ele)

print("The original list is : ", lst)
no_dup_lst = []
[no_dup_lst.append(element) for element in lst if element not in no_dup_lst]
print("The list after removing duplicates : ", no_dup_lst)

