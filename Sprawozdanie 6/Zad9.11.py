class Osoba:
    def __init__(self, idklasy, wiek):
        self._idklasy = idklasy
        self.__wiek = wiek

osoba = Osoba("1C", 16)
print(dir(osoba))
