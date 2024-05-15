class Prostokat:

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Okno:

    def __init__(self, nazwa, kolor, polozenie):

        self.nazwa = nazwa
        self.kolor = kolor
        self.polozenie = polozenie

okno1 = Okno("Okno1", "Biały", Prostokat(0, 0, 100, 200))