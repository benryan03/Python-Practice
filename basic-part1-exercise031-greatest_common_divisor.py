#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
divisor = 0

for x in range (1, max(a, b)):
	if a % x == 0 and b % x == 0:
		divisor = x
	else:
		pass
		
print("Greatest common divisor: " + str(divisor))