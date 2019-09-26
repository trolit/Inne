# zmienna typu bool(przyjmuje 2 wartosci - True lub False)
x = 5 < 6
print(type(x))

# ---------------------------
#     INSTRUKCJE WARUNKOWE
# ---------------------------
# wykorzystamy je gdy chcemy porownywac cos
# i jezeli warunek bedzie prawdziwy to zrobimy
# czynnosc x, gdy natomiast falszywy to albo zero
# reakcji albo wykonany zostanie inny kod

# if czesto stosowany jest w petlach aby podczas
# uzyskania oczekiwanego efektu - wyjsc z niej

# deklaracja, liczbe 10 przypisujemy do zmiennej x
x = 10

# budowa instrukcji warunkowej:
if x == 5:
    print("\nTak,x jest rowne 5")     # ta linijka nalezy do if!
    print("Tak, tak, to tez")         # ta linijka nalezy do if!
else:                                 # else - z angielskiego(ewentualnie)
    print("nie prawda!")

print("\nTa linijka juz nie nalezy do instrukcji warunkowej")

# Uwaga: to co dasz po 4 spacjach(lub 1 tabulator)
# to "należy do instrukcji if, else itd. tak jak
# widać powyżej

# przypomnienie: operator == to operator tzw. equality - sprawdza czy lewa strona jest rowna prawej
# przypomnienie: operator != znak różności, zwraca prawdę jeśli lewa jest różna od prawej i vice versa


#instrukcja warunkowa(przyklad2):
y = 1
# zakomentowalem input aby nie czekac
# y = input()
y = int(y)

if y > 10:
    print("podana liczba jest wieksza od 10")
elif y < 5:
    print("podana liczba jest mniejsza od 5")
else:
    print("podana liczba jest wieksza od 5 ale mniejsza od 10")

# -----------------------------
#            LISTY
# -----------------------------
# mozemy dodawac, usuwac elementy

# lista:
produkty = ["mleko","ser","parowki", "mleko"]

# wypisujemy na ekran pierwszy element listy
print(produkty[0])

# wypisujemy na ekran 2 elementy listy
print(produkty[0:2])

# chcemy do kazdego
# elementu na koncu dodac cos, korzystamy z .
# i uzywamy funkcji z append(laczenia)
produkty.append("szynka")

# aby wyczyscic liste mozemy napisac: produkty.clear()
# mozemy zliczyc ile danego elementu jest w liscie za pomoca funkcji count()
# przyklad:
x = produkty.count("mleko")
print("mamy ", x, " mleka w produktach")  # powinnismy otrzyma 2

print(produkty)

# sprawdzmy typ, otrzymamy class List czyli ok
print(type(produkty))

# dzieki funkcji extend dla list mozemy dac kolejna liste
# extend = rozszerzyc, liste rozszerzamy o kolejna liste
# przyklad:

wiecej_produktow = ["ketchup", "wedlina"]

# rozszerzamy liste produkty o elementy listy wiecej_produktow
produkty.extend(wiecej_produktow)

print(produkty)

# inne funkcje dla list:
# - pop() - usuwanie elementu z listy(podajemy index)
# - remove() - podajemy nazwe obiektu ktory usunac
# - index() - zwraca pozycje danego elementu z listy



# -----------------------------
#            TUPLE
# -----------------------------
# roznia sie tym od list ze nie
# mozna ich edytowac czyli nie mozemy
# usuwac, dodawac elementow
# tuple sa bardziej wydajne(szybsze)
# ale nie mozemy ich edytowac

# przykladowa tupla:
warzywa = ("ogorek", "pomidor", "papryka")

# sprawdzamy typ tupli:
print(type(warzywa))




# -----------------------------
#           SLOWNIKI
# -----------------------------
# def: zestaw kluczy i wartości

# utworzenie slownika person
person = {"wiek": 20, "imie": "Ania"}
# kluczem jest tutaj wiek ,imie
# wartosciami sa tutaj 20, Ania

# sprawdzmy czy jest rzeczywiscie typu slownik(Dict od Dictionary)
print(type(person))

# aby wypisac element ze slownika robimy tak:
print(person["imie"])

# podobny do list i tupli ale w slowniku podajemy
# wlasne klucze, a w listach i tuplach musimy
# poslugiwac sie indeksowaniem liczbowym czyli 0,1,2 itd
# aby dostac sie do elementu

# dla slownika rowniez za pomoca . mozemy wykorzystac
# jakies metody, np. copy, keys itd..

# DO ZAPAMIETANIA:
# Obejmujemy elementy w nawias:
# [ ] jezeli lista, nawiasy kwadratowe
# ( ) jezeli tupla, nawiasy otwarte
# { } jezeli slownik, nawiasy klamrowe
