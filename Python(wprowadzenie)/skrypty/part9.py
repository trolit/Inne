# -------------------------------------------------
#                     WYJĄTKI
# -------------------------------------------------

try:
    plik = open("test.txt", "r")
    plik.write("hello")
    plik.close()

# zlapie wyjatek Pliku nie znaleziono
except FileNotFoundError as e:
    print(e)

# zlapie kazdy wyjatek
except Exception as e:
    print("Wystapil blad!")

# zawsze sie wykona
print("test")




# -------------------------------------------------
#                    OBIEKTOWO
# -------------------------------------------------
#                        +
# -------------------------------------------------
#         METODY MAGICZNE - METODY SPECJALNE
# -------------------------------------------------
#                        +
# -------------------------------------------------
#       TWORZENIE ZMIENNYCH - PARAMETR SELF
# -------------------------------------------------

import foo

# wywolanie funkcji z modulu foo
foo.apple("\nHello")

# odwolanie sie do zmiennej z modulu foo
foo.a = 5

# KLASA - struktura obiektu(np. człowiek - dwie ręce, dwie nogi)

# OBIEKT - utworzenie klasy, konkretny byt z rzeczywistości(np. Tomek)

# METODY MAGICZNE ma wywoływać tylko PyCharm

# parametr self odpowiada za to, że jak mamy np. kilka obiektów jednej klasy
# to PyCharm wie, na którym obiekcie wykonywane są operacje, gdzie jaką wartość
# przechowywać itd, pokazane to zostało na zmiennej liczba poniżej,
# przez self powinno nam się kojarzyć że "ten konkretny obiekt/dla tego konkretnego obiektu)

# tworzenie klas - jak je tworzyć?
# w nawiasie mozemy zapisac z jakiej innej klasy ma ta klasa dziedziczyc
class Calculator():

    # zmienna klasy Calculator
    test = 5

    # tu mozemy podawac funkcje(metody)
    # slowko self jest wazne w prog.obiektowym
    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)
    # jezeli tworzymy metode z dwoma podlogami
    # to znaczy ze bedzie to metoda magiczna(magicmethod)
    def __init__(self):
        self.liczba = 10
        print("Wykonuje sie init!")
    def __del__(self):
        print("Wykonuje sie del!")
    # metoda string wykonuje sie gdy probujemy przekonwertowac metoda na ciag znakow
    def __str__(self):
        return "Hello"

# init - konstruktor
# del - destruktor

# tworzenie obiektu tej klasy i przypisanie go do zmiennej calc
calc = Calculator()

# stworzenie drugiego obiektu
calc2 = Calculator()

# zmienna o nazwie liczba zdefiniowana w "locie"
# nie musimy deklarować w klasie zmiennych ale
# jak ktoś chce to może
calc.liczba = 1

print("Liczba przechowuje = ", calc.liczba + 5)

print("Liczba przechowuje = ", calc2.liczba + 1)

# za pomoca obiektu mozemy teraz odwolywac sie do metod
calc.dodaj(11, 12)

calc2.dodaj(11,11)

# wywola się magiczna metoda str
print(calc)

a = 10
print("a = ", a)
# możemy usunąć zmienną sami
del a


# lista magicznych metod:
# http://farmdev.com/src/secrets/magicmethod/index.html


