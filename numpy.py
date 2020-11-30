import numpy as np
_A = [[6,7,8],
      [8,9,4],
      [5,6,7]]
A = np.array(_A)
print(A)
_B = [[6,4,3],
      [7,8,6],
      [8,6,4]]
B = np.array(_B)
print(B)
print("A + B",A + B)
print("A * B",A * B)
print("ma trận chuyển vị của A là :",A.transpose())
