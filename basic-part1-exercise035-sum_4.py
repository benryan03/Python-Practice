#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a == b or a + b == 5 or max(a, b) - min(a, b) == 5:
	print("True")
else:
	print("False")