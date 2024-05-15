import random

#sprawdza czy sa w ogole
def sprawdz(array, liczba):

    for i in range(len(array)):

        if array[i] == liczba:
            return True

    return False


wylosowane_liczby = random.choices([x for x in range(1,6)], k=4)
print("Wylosowane liczby = ", wylosowane_liczby)
print("Pamiętaj losowane liczby są w zasięgu od 1 do 5 na 4 pozycjach")

wpisane_liczby = [x for x in range(4)]

while(True):
    print("-------------------------------------------------------------")

    #Gracz wpisuje liczby
    for i in range(4):
        wpisane_liczby[i] = int(input('Wpisz liczbę {i}: '.format(i=i)))

    #Liczby są sprawdzane

    #liczby ktore sa w dobrym miejscu
    dobremiejsce = 0
    #liczby ktore sa ale w zlym miejscu
    zlemiejsce = 0
    # liczby ktorych nawet nie ma
    niema = 0
    for x in range(len(wylosowane_liczby)):

        if wylosowane_liczby[x] == wpisane_liczby[x]:
            dobremiejsce += 1
        elif sprawdz(wylosowane_liczby, wpisane_liczby[x]):
            zlemiejsce += 1
        else:
            niema += 1

    if dobremiejsce == len(wylosowane_liczby):
        print("Gratulacje zgadłeś 4 pozycje")
        print("WYGRAŁEŚŚŚŚŚŚŚŚŚ !!!!!!!!!!!")
        break

    print("Jest {dobremiejsce} liczb na dobrym miejscu".format(dobremiejsce = dobremiejsce))
    print("Jest {zlemiejsce} liczb na zlym miejscu".format(zlemiejsce=zlemiejsce))
    print("{niema} liczb nie ma w ogóle".format(niema=niema))