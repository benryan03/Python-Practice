#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#22. Write a Python program to count the number 4 in a given list.

list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
count = 0

for x in list:
	if x == 4:
		count = count + 1
		
print("Found " + str(count) + " instances of 4.")