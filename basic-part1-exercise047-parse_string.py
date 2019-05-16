#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#48. Write a Python program to parse a string to Float or Integer.

a = input("Enter a number: ")

if "." in a:
	a = float(a)
else:
	a = int(a)
	
print (type(a))