#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


if a + b >= 15 and a + b <= 20:
	print("Result: 20")
else:
	print("Result: " + str(a + b))