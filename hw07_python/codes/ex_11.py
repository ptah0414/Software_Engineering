# Write a Python program to concatenate the existing
# dictionaries to create a new one.
# Sample dictionary is 
# Dic1 = {1:10, 2:20} 
# Dic2 = {3:30, 4:40} 
# Dic3 = {5:50, 6:60}
# The result will be {1:10, 2:20, 3:30, 4:40, 5:50, 6;60}

Dic1 = {1:10, 2:20}
Dic2 = {3:30, 4:40}
Dic3 = {5:50, 6:60}

Dic4 = Dic1.copy()
Dic4.update(Dic2)
Dic4.update(Dic3)

print(Dic4)