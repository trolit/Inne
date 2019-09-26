# ------------------------------------
#                PETLE
# ------------------------------------
# def. petla to fragment kodu ktory
# wykonuje sie wiecej razy niz raz

# petla while(/dopóki/)

# deklaracja zmiennej
x = 0

# przykladowa petla wypisujaca na ekran liczby od 0 do 9
while x < 10:
    print(x)
    x += 1

print("koniec petli while..")


# petla nieskoczona:
#while True:
#    print("Petla nieskonczona")

# ------------------------
# petla for(przyklad)
# ------------------------

lista = ["mak", "cukier", "pieczarka"]

print("Przykladowa petla for:")
for slowo in lista:
    print(slowo)
# za kazde slowo w liscie lista wypisz na ekran slowo

# ------------------------
# petla for + if w srodku
# ------------------------

print("Petla for z ifem, wynik:")
for slowo in lista:
    if slowo == "cukier":
        break
    print(slowo)
# wypisze nam tylko i wylacznie mak


# generator, jak podamy range(10) to wygeneruje nam liste 10 elementowa
# jezeli podamy range(10,20) to range wygeneruje nam liste od 10 do 19
for i in range(10):
    print(i)



# FUNKCJA ENUMERATE
# petla for ma ukryty "iterator" - zmienna ktora sie caly
# czas zwieksza

fruits = ["apple", "orange", "apple", "banana", "pear"]

i = 0
# przed przecinkiem liczba
# po przecinku element ktory odczytujemy

print("Rozpoczynam petle z break")

for i, fruit in enumerate(fruits):
    if i == 3:
        break
    print(i)
    print(fruit)

# break - konczenie petli na
print("Koniec")

# inny sposób podstawienia zmiennej do tekstu np.:żądanie
print("Sprawdzam {} i robie {} ".format("testy", "python"))


# continue - ominiecie instrukcji ktore znajduja sie pod nia (tylko dla petli)

print("Rozpoczynam petle z continue")

for i, fruit in enumerate(fruits):
    if i == 2:
        print("Indeks owoca ktory lubie: ", i)
        print("lubie ten owoc - ", fruits[i])
        print("\n\n")
        continue
    print("nie lubie tego owocu - ", fruits[i])



# OPERATORY LOGICZNE
# and (i)
# or (lub)
# not (nie/negacja)

# przykladowe uzycie:
x=2

if x == 5 or x == 2:
    print("\n\nHello")