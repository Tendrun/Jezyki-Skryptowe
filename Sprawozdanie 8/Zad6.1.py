import numpy as np

A = np.array([[1, 2], [4, 5], [7, 8]])
B = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
C = np.array([2, 1, 0])
D = np.array([[3, 2, 1], [0, 5, 6], [8, -1, 2]])

#B + D
if B.shape == D.shape:
    print("B + D = \n", B + D)
else:
    print("Nie można dodać B i D, ponieważ mają różne kształty.")

#3 * A
print("3A = \n", 3 * A)

#-2 * C
print("-2C = \n", -2 * C)

#B * A
if B.shape[1] == A.shape[0]:
    print("BA = \n", B @ A)
else:
    print("Nie można pomnożyć B i A, ponieważ mają niekompatybilne kształty.")


#D * B
if D.shape[1] == B.shape[0]:
    print("DB = \n", D @ B)
else:
    print("Nie można pomnożyć D i B, ponieważ mają niekompatybilne kształty.")


#2 * A + B - C
if A.shape == B.shape:
    AB = A + B
    if B.shape == C.shape:
        print("2A + B - C = \n", 2 * A + B - C)
    else:
        print("Nie można wykonać operacji 2A + B - C, ponieważ macierze mają różne kształty.")
else:
    print("Nie można wykonać operacji 2A + B - C, ponieważ macierze mają różne kształty.")



#C * D - D * C
try:
    if C.shape[1] == D.shape[0]:
        CD = C @ D
        if D.shape[1] == C.shape[0]:
            DC = D @ C
            print("CD - DC = \n", CD - DC)
        else:
            print("Nie można wykonać operacji CD - DC, ponieważ macierze mają różne kształty.")
    else:
        print("Nie można wykonać operacji CD - DC, ponieważ macierze mają różne kształty.")

except IndexError:
    print("Nie można wykonać operacji CD - DC, ponieważ macierze mają różne kształty.")


if D.shape[1] == D.shape[0]:
    print("DD = \n", D @ D)
else:
    print("Nie można pomnożyć D i D, ponieważ mają niekompatybilne kształty.")

#BB + DD
if B.shape[1] == D.shape[0]:
    BB = B @ B
    if D.shape[1] == D.shape[0]:
        DD = D @ D
        if BB.shape[1] + DD.shape[0]:
            print("BB + DD= \n", BB + DD)
        else:
            print("Nie można wykonać operacji BB + DD, ponieważ macierze mają różne kształty.")
    else:
        print("Nie można wykonać operacji BB + DD, ponieważ macierze mają różne kształty.")
else:
    print("Nie można wykonać operacji BB + DD, ponieważ macierze mają różne kształty.")

#4 * A
print("4A = \n", 4 * A)

# A * B
if A.shape[1] == B.shape[0]:
    print("AB = \n", A @ B)
else:
    print("Nie można pomnożyć A i B, ponieważ mają niekompatybilne kształty.")

#B * B
if B.shape[1] == B.shape[0]:
    print("B^2 = \n", np.power(B, B))
else:
    print("Nie można pomnożyć B i B, ponieważ mają niekompatybilne kształty.")

#A * A
if A.shape[1] == A.shape[0]:
    print("A^2 = \n", A @ A)
else:
    print("Nie można pomnożyć A i A, ponieważ mają niekompatybilne kształty.")

#C / C
try:
    if C.shape[1] == C.shape[0]:
        print("C/C = \n", C / C)
    else:
        print("Nie można podzielić C przez C, ponieważ zawiera zera.")
except IndexError:
    print("Nie można podzielić C przez C, ponieważ zawiera zera.")
