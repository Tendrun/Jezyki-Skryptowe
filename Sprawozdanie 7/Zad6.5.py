class Osoba:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

class Employee(Osoba):
    def __init__(self, name, lastname, age, salary, position):
        super().__init__(name, lastname, age)
        self.salary = salary
        self.position = position

emp1 = Employee("Edek", "Kret", 21, 8000, "Programista")