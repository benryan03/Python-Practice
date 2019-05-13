#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#7. Write a Python program to accept a filename from the user and print the extension of that.
#
#This will work for any extension length (at least 1 character)
#Still need to add error for input with no extension found


result = False
x = -1
y = 1

filename = input("Enter a filename: ")
filename = filename[::-1] #reverses filename
while result == False:
	x = filename.find(".", 0, y)
	if x == -1:
		y = y + 1
		continue
	elif x == y:
		result = True
	break
extension = filename[0:y]
extension = extension[::-1] #reverses extension
print("Extension: " + (extension))