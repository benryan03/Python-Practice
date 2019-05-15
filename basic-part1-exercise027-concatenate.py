#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#27. Write a Python program to concatenate all elements in a list into a string and return it.

list = [1, 2, 3, "a", "b", "c"]
string = ""
count = 0

for x in list:
	string = string + str(list[count])
	count = count + 1
	
print(string)