import random
import statistics

slownik = \
    [
            { "imie": "Jan", "nazwisko": "Kowalski", "wiek": 15, "oceny":
                [random.randrange(2,5) for x in range(10)]},
            { "imie": "Ania", "nazwisko": "Tadeusz", "wiek": 13, "oceny":
                [random.randrange(2,5) for x in range(10)]},
            { "imie": "Norbert", "nazwisko": "Greczyn", "wiek": 16, "oceny":
                [random.randrange(2,5) for x in range(10)]},
    ]

sredniaocenstudenta = [{"imie": x["imie"], "nazwisko": x["nazwisko"], "srednia": sum(x["oceny"])/len(x["oceny"])} for x in slownik]
sredniaocenstudentow = [sum(x["oceny"])/len(x["oceny"]) for x in slownik]
medianawieku = statistics.median([x["wiek"] for x in slownik])
dlugoscnazwisk = statistics.median([len(x["nazwisko"]) for x in slownik])

print("Mediana dlugosci nazwisk kazdego studenta = ", dlugoscnazwisk)
print("Mediana wieku kazdego studenta = ", medianawieku)
print(medianawieku, sep='\n')
print(*sredniaocenstudenta, sep='\n')
print(*slownik, sep='\n')