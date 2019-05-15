#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#25. Write a Python program to check whether a specified value is contained in a group of values.

list = [1, 3, 5, 7, 9, 11, 13, 15, 19]

x = int(input("Enter a number: "))

if x in list:
	print(str(x) + " is in the list.")
else:
	print(str(x) + " is not in the list.")