lokalizacja_pliku = input("Podaj lokalizacja pliku: ")

try:
    otwary_plik = open(lokalizacja_pliku, mode="r")
except FileNotFoundError:
    print("Nie znaleziono pliku")
    exit()

tekst = otwary_plik.read()

print(tekst)