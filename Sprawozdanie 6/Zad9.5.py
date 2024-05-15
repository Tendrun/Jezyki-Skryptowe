def dodaj(x,y):
    return x+y

def odejmij(x,y):
    return x-y

def pomnoz(x,y):
    return x*y

def podziel(x,y):
    return x/y


x = dodaj(
        podziel(
            pomnoz(
                dodaj(4,2),
                    odejmij(5,10)),
                odejmij(
                    pomnoz(32, 11), 4)),
    2)

print(x)