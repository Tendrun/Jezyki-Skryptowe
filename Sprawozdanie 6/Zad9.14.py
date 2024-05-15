class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Student(Osoba):
    def __init__(self, imie, nazwisko, nr_ind, oceny):
        Osoba.__init__(self, imie, nazwisko)
        self.nr_ind = nr_ind
        self.oceny = oceny


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, stanowisko, wynagrodzenie):
        Osoba.__init__(self, imie, nazwisko)
        self.stanowisko = stanowisko
        self.wynagrodzenie = wynagrodzenie


class PracujacyStudent(Student, Pracownik):
    def __init__(self, imie, nazwisko, stanowisko, wynagrodzenie, nr_ind, oceny):
        Pracownik.__init__(self, imie, nazwisko,stanowisko, wynagrodzenie)
        Student.__init__(self, imie, nazwisko, nr_ind, oceny)


WS = PracujacyStudent("Jan", "Kowalski", "Programista", 10000,
                                    10, [5,5,3,5,4])

print(f"imie {WS.imie} - nazwisko {WS.nazwisko} - stanowisko {WS.stanowisko} - wynagrodzenie {WS.wynagrodzenie}"
      f" - numer indeksu {WS.nr_ind} - oceny {WS.oceny}")