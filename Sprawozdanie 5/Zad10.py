def StworzZamowienie(imie, nazwisko, zamowienia):
    tresc = ""
    powitanie = "Witaj {imie} {nazwisko} \n".format(imie=imie, nazwisko=nazwisko)
    towary = "Oto szczegóły twojego zamówienia:\n"
    Sumacen = 0
    for zamowienie in zamowienia:
        towary += "{towar}, szt {szt}, cena {cena}, razem {razem}\n".format(towar=zamowienie['nazwa'],
                                                                           szt=zamowienie['ilosc'],
                                                                           cena=zamowienie['cena'],
                                                                           razem=zamowienie['ilosc'] * zamowienie[
                                                                               'cena'])
        Sumacen += zamowienie['ilosc'] * zamowienie['cena']

    pozegnanie = "Pozdrawiamy {nazwasklepu}\n".format(nazwasklepu="Fajny Sklep")

    Suma = "Suma {suma}\n".format(suma=Sumacen)
    tresc = powitanie + towary + Suma + pozegnanie
    return tresc



zamowienia = [{'nazwa': 'książka', 'ilosc': 1, 'cena': 199.99}, {'nazwa': 'zeszyt', 'ilosc': 2, 'cena': 7.89}]
suma = 215.77
sklep = "TwojFantastycznySklep"

print(StworzZamowienie("Jan", "Kochanowski" ,zamowienia))
