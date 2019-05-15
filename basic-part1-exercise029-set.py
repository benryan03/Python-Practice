#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
set = set()

for x in color_list_1:
	if x not in color_list_2:
		#print(x + "not in 2")
		set.add(x)
	elif x in color_list_2:
		#print(x + "in 2")
		pass
		
print(set)