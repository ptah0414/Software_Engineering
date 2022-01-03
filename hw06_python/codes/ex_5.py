# Write a Python program to replace the last value of tuples
#  in a list [(10, 20, 30),(40,50,60),(70,80,90)] to a list [(10, 20, 30),(40,50,60),(70,80,100)]

a = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
b = []
c = []


for i in range(len(a)):
    b.append(list(a[i]))
    
b[2][2] = b[2][2] + 10

for i in range(len(b)):
    c.append(tuple(b[i]))
    
print(c)