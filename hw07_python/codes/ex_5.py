# Write a Python program which solves the equation. 
# 2x + 3y = 10
# 4x + 2y = 4

import numpy as np

A = np.array([[2, 3], [4, 2]])
B = np.array([10, 4])
C = np.linalg.solve(A, B)

print(C)