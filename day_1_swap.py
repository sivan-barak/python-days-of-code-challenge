#Create a program that swaps the values of two variables.

def swap_values(x, y):
    print("Before values swap: ", x, y)
    x, y = y, x
    print("After values swap: ", x, y)

print("This program swaps between two given values")
val1 = input("Enter a value: ")
val2 = input("Enter another value: ")
swap_values(val1, val2)
