class Osoba:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastname

    def getAge(self):
        return self.age

class Student(Osoba):
    def __init__(self, indexNr, name, lastname, age):
        super().__init__(name, lastname, age)
        self.indexNr = indexNr

    def getIndexNr(self):
        return self.indexNr
