#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b or a == c or b == c:
	print("Result: 0")
else:
	print("Result: " + str(a + b + c))