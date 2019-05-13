#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

x = int(input("Enter an integer: "))
print("Result: " + str(x + int(str(x) + str(x)) + int(str(x) + str(x) + str(x))))