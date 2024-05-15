plik = open("plik.txt", mode="r")

nazwa_pliku = input("Podaj nazwe pliku: ")

linie = plik.readlines()

for i in range(0, len(linie)):
    if i % 2 == 0:
        linie[i] =  linie[i].join('!') + linie[i]
    else:
        linie[i] = linie[i].join('?') + linie[i]


plik_zapis = open(nazwa_pliku, mode="w")
plik_zapis.writelines(linie)