#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

n = int(input("Enter a non-negative integer: "))
string1 = input("Enter a string: ")
string2 = string1

if len(string1) >= 2:
	string2 = string1[0:2]
	for x in range(1, n):
		string2 = string2 + string1[0:2]
elif len(string1) == 1:
	for x in range(1, n):
		string2 = string2 + string1
else:
	print("Error: Non-negative integer not entered.")
	
print(string2)