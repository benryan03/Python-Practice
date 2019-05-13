#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#12. Write a Python program to print the calendar of a given month and year.

import calendar

for x in calendar.Calendar().itermonthdates(2019, 5):
	print(x)