#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#7. Write a Python program to accept a filename from the user and print the extension of that.
#
#This will work for any extension length (at least 1 character)

z = -1
y = 1
extension = ""

filename = input("Enter a filename: ")
filename = filename[::-1] #reverses filename

for x in filename:
	z = filename.find(".", 0, y)
	if z == -1: #if character is not a period
		y = y + 1
	else: #if character is a period
		extension = filename[0:y]
		extension = extension[::-1] #reverses extension
		print("Extension: " + (extension))
		break

if extension == "":
	print("Extension not found in filename.")
