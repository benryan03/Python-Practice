#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#17. Write a Python program to test whether a number is within 100 of 1000 or 2000. Go to the editor

x = int(input("Enter a number: "))

if x >= 900 and x <= 1100:
	print(str(x) + " is within 100 of 1,000.")
elif x >= 1900 and x <= 2100:
	print(str(x) + " is within 100 of 3,000.")
else:
	print(str(x) + " is not within 100 of 1,000 or 2,000.")