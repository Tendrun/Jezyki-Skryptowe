import numpy as np

# Definiowanie macierzy
A = np.array([[1, 2], [4, 5], [7, 8]])
B = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
C = np.array([2, 1, 0])
D = np.array([[3, 2, 1], [0, 5, 6], [8, -1, 2]])

# Obliczanie śladu dla każdej macierzy
trace_A = np.trace(A)
trace_B = np.trace(B)
try:
    trace_C = np.trace(C)
except ValueError:
    trace_C = None
trace_D = np.trace(D)

print(f"Ślad macierzy A: {trace_A}")
print(f"Ślad macierzy B: {trace_B}")
print(f"Ślad macierzy C: {trace_C}")
print(f"Ślad macierzy D: {trace_D}")