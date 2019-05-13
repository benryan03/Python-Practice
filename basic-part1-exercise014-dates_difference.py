#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#14. Write a Python program to calculate number of days between two dates.

import datetime

#Gets date inputs as text from user
input1 = input("Enter first date (format YYYYMMDD): ")
input2 = input("Enter second date (format YYYYMMDD): ")

#Converts inputs to date/time objects
date1 = datetime.datetime(int(input1[0:4]), int(input1[4:6]), int(input1[6:8]))
date2 = datetime.datetime(int(input2[0:4]), int(input2[4:6]), int(input2[6:8]))

#Finds difference between date/time objects and prints final output
print("Difference: " + str(date2-date1))