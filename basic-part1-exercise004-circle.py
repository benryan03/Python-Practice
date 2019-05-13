#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#4. Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

radius = int(input(("Enter radius: ")))
print("Area: " + str(((radius * radius) * math.pi)))
