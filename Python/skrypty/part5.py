# PART 5
# FUNKCJE
# def. część/fragment kodu który spełnia
# daną czynność lub wykonuje dane zadanie
# funkcje są po to aby zmniejszyć powtarzalność
# kodu ale też po to aby zwiększyć czytelność
# kodu


# przykladowa funkcja
# slowko def = define

# end='' spowoduje ze nie bedzie lamal linii
# z kolejnymi wywolaniami funkcji

def printme():
    print("Hello: ", end='')

# wywolanie funkcji
printme()
printme()


# funkcja mnozaca dwie liczby

def mnoz(a, b):
    print("\nWynik a*b = ", a * b)

mnoz(4,5)


# funkcja zwracajaca, Jezeli cos zwraca to musimy
# wartosc zwracana gdzies zapisac aby nie uciekla

def dodaj(a, b):
    return a + b

wynik = dodaj(2,3)
print("Wynik dodawania: ", wynik)


# podanie w innej kolejnosci argumentow:
wynik = dodaj(b=3, a=1)
print("Wynik dodawania: ", wynik)


# opcjonalny argument - aby go nadac musimy
# podac wartosc domyslna przy tworzeniu funkcji
# jeżeli nie podamy w te miejsce wartosci to wtedy
# pycharm skorzysta z opcjonalnego argumentu

def funckjazOpcjonalnym(a, b=5):
    return a + b

wynik = funckjazOpcjonalnym(4)
print("Wynik funkcji opcjonalnej: ", wynik)