import math

class Punkt:
    def __init__(self, x,y):
        self.x=x
        self.y=y

    def wyswietl(self):
        print("Punkt znajduje się na x = " + self.x + " y = " + self.y)

class Odcinek:
    def __init__(self, punkt1, punkt2):
        self.punkt1 = punkt1
        self.punkt2 = punkt2

    def dlugosc(self):
        return math.sqrt( (self.punkt2.x - self.punkt1.x)**2 + (self.punkt2.y - self.punkt1.y)**2 )


class Trojkat:
    def __init__(self, punkt1, punkt2, punkt3):
        self.sciana1 = Odcinek(punkt1, punkt2)
        self.sciana2 = Odcinek(punkt1, punkt3)
        self.sciana3 = Odcinek(punkt2, punkt3)

        print(self.sciana1.dlugosc(), " " , self.sciana2.dlugosc() , "  " , self.sciana3.dlugosc() , "")


    def obwod(self):
        return self.sciana1.dlugosc() + self.sciana2.dlugosc() + self.sciana3.dlugosc()


    def Pole(self):
        p = self.obwod()

        p = math.sqrt(p * (p - self.sciana1.dlugosc()) * (p - self.sciana1.dlugosc()) *
                      (p -  self.sciana1.dlugosc()))


trojkat = Trojkat(Punkt(0,0), Punkt(2,2), Punkt(4,4))

print(trojkat.obwod())