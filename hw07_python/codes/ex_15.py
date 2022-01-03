# Write a Python program to reverse the order of the items in the array
# Sample array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])

from array import *

a = array("i", [1, 3, 5, 3, 7, 1, 9, 3])
b = array("i", [0, 0, 0, 0, 0, 0, 0, 0])


for i in range(len(a)):
    b[len(a)-i-1] = a[i]
    
print(b)