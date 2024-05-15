import __init__ as init

def dodaj(x, y):
    return [[x[j][i] + y[j][i] for i in range(len(x))]
            for j in range(len(y)) if len(x) == len(y) and len(x[0]) == len(y[0])]

def odejmowanie(x, y):
    return [[x[j][i] - y[j][i] for i in range(len(x))]
            for j in range(len(y)) if len(x) == len(y) and len(x[0]) == len(y[0])]

def pomnoz(x, y):

    matrix = [[0] * len(x) for i in range(len(y))]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y[0])):
                matrix[i][j] += x[i][k] * y[k][j]

    return matrix