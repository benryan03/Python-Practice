#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#36. Write a Python program to add two objects if both objects are an integer type.

a = input("Enter something: ")
b = input("Enter something else: ")

try:
	a = int(a)
except ValueError:
	pass
	
try:
	b = int(b)
except ValueError:
	pass

if type(a) == int and type(b) == int:
	print("Result: " + str(a + b))
else:
	print("One or more inputs is not an int.")