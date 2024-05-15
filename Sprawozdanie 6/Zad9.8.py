lista = lambda i : [i for i in range(10) if i % 2 == 0]
print("funkcja lambda = ", lista(10))

def Parzyste(i):
    if i % 2 == 0:
        return i

mapa = list(map(Parzyste, range(10)))
mapa = [x for x in mapa if x is not None]
print("funkcja map = ", mapa)