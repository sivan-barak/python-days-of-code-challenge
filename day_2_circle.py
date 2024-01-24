#Create a program to calculate the area of a circle given its radius.

import math

def calc_circle_from_radius(rad):
    return math.pi*rad**2

print("This program will calculate the area of a circle given its radius")
radius = float(input("Please enter radius of a circle: "))
circle_area = calc_circle_from_radius(radius)
print("The area of a circle with radius {} is {}".format(radius, circle_area))