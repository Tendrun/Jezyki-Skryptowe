class Osoba:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

class Employee(Osoba):
    def __init__(self, name, lastname, age, salary, position):
        Osoba.__init__(self, name, lastname, age)
        self.salary = salary
        self.position = position

class Student(Osoba):
    def __init__(self, indexNr, name, lastname, age):
        Osoba.__init__(self, name, lastname, age)
        self.indexNr = indexNr

    def getIndexNr(self):
        return self.indexNr

class WorkingStudent(Student, Employee):
    def __init__(self, indexNr, name, lastname, age, salary, position):
        Student.__init__(self, indexNr, name, lastname, age)
        Employee.__init__(self, name, lastname, age, salary, position)

working_student = WorkingStudent("1092", "Jan", "Kowalski", 30, 3000, "Intern")