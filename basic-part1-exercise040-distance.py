#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math

point_1_x = int(input("Enter X-value for point 1: "))
point_1_y = int(input("Enter Y-value for point 1: "))
point_2_x = int(input("Enter X-value for point 2: "))
point_2_y = int(input("Enter Y-value for point 2: "))

distance = math.sqrt((point_2_x - point_1_x)**2 + (point_2_y - point_1_y)**2)

print("Distance: " + str(distance))