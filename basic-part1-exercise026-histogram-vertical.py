#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#25. Write a Python program to check whether a specified value is contained in a group of values.

list = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 8]
list.sort()

min = list[0]									#Minimum value of X-axis (must appear in list)
max = list[-1]									#Maxumum value of X-axis (must appear in list)

#Calculates maximum height of Y-axis
max_range = 0
for x in range(min,(max + 1)):
	if list.count(x) > max_range:
		max_range = list.count(x)

#Graph loop
print("")										#Print empty line for padding
for x in range(max_range, 0, -1):				#Loop backwards from maximum height of Y-axis
	current_iteration = x						
	for y in range(min,(max + 1)):				
		if current_iteration == list.count(y):	#If backwards number of loop (the current Y-axis height) equals the number of times that number appears in the list:
			print("X ", end='')					#Than X is printed
		else:									
			print("  ", end='')					
	print("")									

#Prints numbers on X-axis
for x in range(min,(max + 1)):
	print(str(x) + " ", end='')