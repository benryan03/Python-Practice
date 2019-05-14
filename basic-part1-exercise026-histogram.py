#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#25. Write a Python program to check whether a specified value is contained in a group of values.

list = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 8]

min = list[0]
max = list[-1]

for x in range(min,(max + 1)):
	print(str(x) + " ", end='')
	for y in list:
		if x == y:
			print("X", end='')
	print("")