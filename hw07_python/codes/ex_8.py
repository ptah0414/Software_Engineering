# Write a Python program to sort a tuple by its float element from a list of tuple 
# [(‘item1’,10.5), (‘item2’,11.8),(‘item3’,9.1) (‘item4’,7.3)]
 
a = [("item1", 10.5), ("item2", 11.8), ("item3" ,9.1), ("item4", 7.3)]

a.sort(key=lambda x:x[1])
print(a)
