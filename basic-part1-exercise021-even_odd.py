#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

x = int(input("Enter a number: "))

if x % 2 == 0:
	print(str(x) + " is even.")
else:
	print(str(x) + " is odd.")