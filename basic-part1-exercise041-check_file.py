#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#41. Write a Python program to check whether a file exists.

import os

x = input("Enter filename to check: ")

print(os.path.exists(x))