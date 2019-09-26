# PYTHON - WPROWADZENIE
# WYPIS NA EKRAN
# ZMIENNE
# KONWERSJE ZMIENNYCH

# -------------------------------
# WYPISANIE NA EKRAN INFORMACJI
# -------------------------------

# aby wypisac tekst(czyli string):
print("\nTo jest tekst, tekst zapisujemy w cudzyslowach")

# tu wypisaliśmy na ekran liczbę 50
print(50)

# tu wypisaliśmy na ekran łańcuch(string) który składa się ze ZNAKU 5 i ZNAKU 0!!
print("50")

# -------------------------------
#             ZMIENNE
# -------------------------------

# warto pamietac!
# python automatycznie konwertuje zmienne
# jedni uwazaja to za zalete a inni jako
# wadę(bo zużywa cenne zasoby na to)

# LICZBA
x = 5        # to zmienna typu int(od integer czyli liczba calkowita)
# pamiętamy, że = to tzw. operator przypisania(przypisuje prawo do lewego)

# aby ją wypisać(jako liczbe):
print(x)

# aby sprawdzic typ zmiennej to musimy
# napisac np. print(type(x))

print(type(x))

# kolejna zmienna typu int
y = 5

# przykladowe operacje na liczbach:
print("wynik x+y = ", x+y)
print("wynik x*y = ", x*y)

# float - liczby zmiennoprzecinkowe
liczba = 5.5

print("liczba ma wartosc: ", liczba)

# powinien wyswietlic class 'float'
print("typ zmiennej liczba to", type(liczba))

# -------------------------------
#        KONWERSJA ZMIENNYCH
# -------------------------------

# zapisanie tekstu do zmiennej(zapisujemy tekst w cudzyslowiu)
tekst = "to jest moj tekst"

# sprawdzamy typ zmiennej
print(type(tekst))
# wienym ze zwroci: str czyli string czyli łańcuch czyli ciąg znaków

# dodajemy kolejny ciag znakow do zmiennej tekst:
tekst = tekst + " i dodatek"

# co przechowuje zmienna tekst - wypiszmy na ekran?
print(tekst)

# FUNKCJA INPUT
# funkcja input - wczytywanie od uzytkownika
# gdy kompilator ja napotka, zatrzymuje sie
# i czeka az cos uzytkownik wpisze
# musimy wtedy kliknac na ekran konsoli, ktora
# pokazuje efekt dzialania naszego kodu i podac cos

zmienna = input()

print("podales pod zmienna: ", zmienna, "ktora jest typu: ", type(zmienna))

# Uwaga: input bierze "ciag znakow", zatem nie mozemy na tym wykonac operacji
# matematycznej! Podobnie jak w C# gdzie Console.ReadLine bierze łańcuch, a żeby
# pobrać liczby to musieliśmy skonwertować..

# konwertujemy string na int zmiennej o nazwie "zmienna"
zmienna = int(zmienna)
# zatem mozemy wykonywac operacje na liczbach calkowitych
# gdybysmy podali przecinkowa liczbe - dostaniemy blad
# musielibysmy skonwertowac do float a nie do int

# zobaczmy efekt naszej konwersji:
print("podales pod zmienna: ", zmienna, "ktora jest typu: ", type(zmienna))

# i teraz mozemy na zmiennej robic operacje matematyczne
zmienna = zmienna * 2
print(zmienna)




# -------------------------------------------
#   MANIPULACJA STRINGAMI(CIAGAMI ZNAKOW)
# -------------------------------------------

tekst = "Ala ma kota, a kot ma Ale ;)"

print(tekst)

# jak wypisac pierwszy element lancucha - tekst?
print(tekst[0])
# uzyskamy w ten sposob A, pamietamy, ze numerowanie
# w wielu jezykach jest od 0!

# nie musimy oczywiście odrazu wypisywac na ekran, mozemy
# przypisac do kolejnej zmiennej nasza literke czy wycinek

y = tekst[5]
# zapisujemy do zmiennej y 5 znak z lancucha "tekst"s

# co wyswietli to hmm?
print(tekst[1-5])
# odp: ostatnia litere e!
# zauwaz, 1-5 = -4 i cofamy sie do tylu o 4 miejsca zaczynajac od 0
# czyli zobaczmy:
# A to 0
# ) to -1
# ; to -2
# <spacja> to -3
# e to -4
# zgadza sie

# jak wyswietlic kawalek lancucha(ciagu znakow) ?
# przypomina Haskella z tym : w nawiasach kwadratowych :)
print(tekst[0:6])

# gdy damy np.
print(tekst[:7])
# to chcemy wypisac z lancucha "tekst" znaki od 0 do 7






