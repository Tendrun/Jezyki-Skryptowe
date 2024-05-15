import numpy as np

A = np.array([[1, 2], [4, 5], [7, 8]])
B = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
C = np.array([2, 1, 0])
D = np.array([[3, 2, 1], [0, 5, 6], [8, -1, 2]])

A_T = A.transpose()
B_T = B.transpose()
C_T = C.transpose()
D_T = D.transpose()

print("Transpozycja A = \n", A_T)
print("Transpozycja B = \n", B_T)
print("Transpozycja C = \n", C_T)
print("Transpozycja D = \n", D_T)