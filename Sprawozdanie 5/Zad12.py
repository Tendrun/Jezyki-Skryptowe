lokalizacja_pliku = input("Podaj lokalizacja pliku: ")

otwary_plik = open(lokalizacja_pliku, mode="r")

tekst = otwary_plik.read()

print(tekst)