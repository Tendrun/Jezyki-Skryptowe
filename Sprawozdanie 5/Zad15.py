lokalizacja_pliku = input("Podaj lokalizacja pliku: ")

linijkaDoOdczytuj = int(input("Podaj linijke ktora odczytac: "))

try:
    otwary_plik = open(lokalizacja_pliku, mode="r", encoding="utf-8")
except FileNotFoundError:
    print("Nie znaleziono pliku")
    exit()

tekst = otwary_plik.readlines()

print(tekst[1])