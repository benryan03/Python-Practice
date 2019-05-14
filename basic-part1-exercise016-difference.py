#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

x = int(input("Enter a number: "))

if x < 17:
	print("Result: " + str(17 - x))
else:
	print("Result: " + str(2*(x - 17)))