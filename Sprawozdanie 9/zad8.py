import numpy as np

pi = np.pi
print(f"Wartość stałej π: {pi}")

wynik = np.sin(pi)
print(f"Wartość sin(π): {wynik}")

if wynik == 0:
    print("Wynik jest równy 0.")
else:
    print("Wynik nie jest równy 0.")
