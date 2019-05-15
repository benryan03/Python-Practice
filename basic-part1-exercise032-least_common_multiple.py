#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#32. Write a Python program to get the least common multiple (LCM) of two positive integers.

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

lcm = 0
multiplier = 1

while lcm == 0:
	if max(a, b) * multiplier % min(a, b) ==  0:
		lcm = max(a, b) * multiplier
		break
	else:
		multiplier = multiplier + 1

print("Least common multiple: " + str(lcm))