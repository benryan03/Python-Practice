#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

x = int(input("Enter a number: "))

if x % 2 == 0:
	print(str(x) + " is even.")
else:
	print(str(x) + " is odd.")