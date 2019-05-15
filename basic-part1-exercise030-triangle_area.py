#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#30. Write a Python program that will accept the base and height of a triangle and compute the area.

base = int(input("Enter triangle base: "))
height = int(input("Enter triangle height: "))

area = (.5 * base) * height

print("Triangle area: " + str(area))