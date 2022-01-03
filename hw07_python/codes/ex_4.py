# Write a Python program to extract numbers from a strig “a1a2a3a4a5” and print those numbers.

a = "a1a2a3a4a5"
b = ""

for i in range(len(a)):
    if a[i].isnumeric() == True:
        b = b + a[i]
        
print(b)