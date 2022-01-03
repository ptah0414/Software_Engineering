#  Exercise 10) Write a Python program to add members in a set
#  {“Monday”,”Tuesday”,”Wednesday”,”Thursday”,”Friday”}. 
#  Note adding string in Python means concatenating strings.

a = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}

a.update(["Saturday", "Sunday"])
print(a)