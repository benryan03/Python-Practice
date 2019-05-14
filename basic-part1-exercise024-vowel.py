#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#24. Write a Python program to test whether a passed letter is a vowel or not.

x = input("Enter a letter: ")

if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
	print("Vowel!")
elif x == "y":
	print("Sometimes a vowel!")
else:
	print("Not a vowel!")