import importlib

import myalgebra as alg

wektor = []

while True:
    x = input("Podaj element wektora lub 'K' aby zakończyć: ")
    if x.upper() == 'K':
        break
    else:
        wektor.append(float(x))
        importlib.reload(alg)