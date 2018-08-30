# -----------------------------------------------
#   MODUŁ OS, TWORZENIE FOLDEROW i listy plików
# -----------------------------------------------

import os
# importujemy moduł os, dzieki czemu mamy dostep do
# ciekawych funkcji

# funkcja do listowania plików i katalogów
lista = os.listdir("C:/Windows")
print(lista)

# gdybyśmy chcieli wylistować bieżący katalog to wystarczy napisać . czyli tak:
lista = os.listdir(".")
print(lista)

print("\n\n")

# napiszmy teraz pętlę for która sprawdzi
# czy aktualnie brana rzecz z biezacego katalogu jest plikiem czy katalogiem
for item in os.listdir("."):
    if os.path.isfile(item):
        print(item, " jest plikiem")
    elif os.path.isdir(item):
        print(item, " jest katalogiem")


# funkcja do zmiany nazwy pliku:
# os.rename("nazwa_pliku", "nowa_nazwa")

# funkcja do usuniecia pliku:
# os.remove("nazwa_pliku")

# funkcja do usuniecia folderu:
# os.rmdir("nazwa_folderu")

# tworzenie folderu:
# os.mkdir("nazwa_folderu")
