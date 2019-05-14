#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

string = input("Enter a string: ")

if string[0:2] == "Is":
	pass
else:
	string = "Is " + string

print(string)