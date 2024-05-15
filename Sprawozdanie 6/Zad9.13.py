class Prostokat:

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Okno(Prostokat):

    def __init__(self, nazwa, kolor,x,y,w,h):
        super().__init__(x,y,w,h)

        self.nazwa = nazwa
        self.kolor = kolor

okno1 = Okno("Okno1", "Biały", 0, 0, 100, 200)