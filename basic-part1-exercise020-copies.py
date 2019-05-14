#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

string1 = input("Enter a string: ")
n = int(input("Enter a non-negative integer: "))

string2 = string1

for x in range(1, n):
	string2 = string2 + string1
	
print(string2)