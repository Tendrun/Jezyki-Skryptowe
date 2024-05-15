class Osoba:
    def init (self, imie="Jan", nazwisko="Kowalski" ):
        self.imie = imie
        self.nazwisko = nazwisko
    def przywitaj(self):
        print("Witaj" + self.imie+" "+self.nazwisko )

print(type(print))
print(type(Osoba))

