#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))

if number1 == number2 == number3:
	print("Result: " + str(3 * (number1 + number2 + number3)))
else:
	print("Sum: " + str(number1 + number2 + number3))