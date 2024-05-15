class Wektor:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Wektor(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return Wektor(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Wektor(self.x * other.x, self.y * other.y)

    def __productHardmad__(self, other):
       return Wektor(self.x * other.x, self.y * other.y)

    def __str__(self):
        return f'x = {self.x} y = {self.y}'

Wektor1 = Wektor(1,2)
Wektor2 = Wektor(4,3)
print(Wektor1 + Wektor2)
print(Wektor1 - Wektor2)
print(Wektor1 * Wektor2)
print(Wektor1.__productHardmad__(Wektor2))
print(Wektor1)