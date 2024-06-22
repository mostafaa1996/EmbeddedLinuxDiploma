#!/usr/bin/python3
#Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
Radius = float(input("Enter your radius here in cm:  "))
print(f"The area of the circle is : {math.pi * (Radius**2)} cm2")