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



Student1 = Student("Piotrek", "Kowalski", Note({"Matematyka":3, "Polski":3,"Geografia":1, "Informatyka": 4}))
Student2 = Student("Maciej", "Radczyc", Note({"Matematyka":1, "Polski":5,"Geografia":5, "Informatyka": 4}))

