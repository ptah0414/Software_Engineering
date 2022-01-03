# Write a Python program to append a new item 11 to the end of the array.
# Original array: array('i', [1, 3, 5, 7, 9]) 
# Output array: array('i', [1, 3, 5, 7, 9, 11])

from array import *

a = array("i", [1, 3, 5, 7, 9])

a.append(11)
print(a)