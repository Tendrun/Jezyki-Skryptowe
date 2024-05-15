class Note:
    def __init__(self, ocena):
        self.ocena = ocena

    def __str__(self):
        return str (self.ocena)

class Student:

    def __init__(self, imie, nazwisko, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = oceny

    def __str__(self):
        return f'imie = {self.imie}, nazwisko = {self.nazwisko}, oceny = {self.oceny}'

class Group:
    def __init__(self, lista_studentow):
        self.lista_studentow = lista_studentow


    def zapisz_plik(self):
        with open("Plik.txt", mode="w") as plik:
            for student in self.lista_studentow:
                plik.write(str(student) + '\n')

Studenci = {Student("Piotrek", "Kowalski", Note({"Matematyka":3, "Polski":3,"Geografia":1})),
            Student("Maciej", "Radczyc", Note({"Matematyka":1, "Polski":5,"Geografia":5})),
            Student("Mateusz", "Majcer", Note({"Matematyka":5, "Polski":5,"Geografia":5}))
            }

group = Group(Studenci)
group.zapisz_plik()