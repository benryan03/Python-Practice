#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

amount = float(input("Enter principal amount: "))
interest = float(input("Enter interest rate (""1"" = 1 percent): "))
years = int(input("Enter number of years (integer): "))

for x in range (0, years):
	amount = amount + (amount * (interest * .01))
	
print("Final amount: " + str(amount))