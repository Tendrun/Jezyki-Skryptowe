import __init__ as init
def dodaj(x, y):
    return [x[i]+y[i] for i in range(len(x)) if len(x) == len(y)]

def pomnoz(x, y):
    return [x[i]*y[i] for i in range(len(x)) if len(x) == len(y)]

def odejmowanie(x, y):
    return [x[i]-y[i] for i in range(len(x)) if len(x) == len(y)]