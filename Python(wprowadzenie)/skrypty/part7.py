# -----------------------------
#        OBSLUGA PLIKOW
#       TRYBY WRITE, READ
# -----------------------------
# Wczytywanie i zapisywanie do pliku


# aby otworzyć plik - polecenie open
# kolejny argument mode - jeżeli nie wpiszemy trybu to domyślnie będzie r - read(tylko do odczytu, jesli nie
# odnajdzie pliku to wywali blad) zatem nie mozemy nic w takim trybie zapisac do takiego pliku. Musimy narzucic
# tryb
# link do tabelki z trybami: https://docs.google.com/spreadsheets/d/1uVWg1DFioZXymNY7eorothGvAhOfgcunXf_Myncw4B0/edit#gid=0

f = open("plik.txt", "a+")
# tworzymy uchwyt do pliku aby zapisac wynik(pod zmienna f)

# zapisanie do pliku
f.write("\n123 ")
# zamykamy plik aby inne programy do niego mialy dostep itd..
f.close()

# ----------------------------------------------------------------------------------
f = open("plik.txt")
# gdy chcemy odczytac cos z pliku np. kilka okreslonych znakow
print(f.read(5))

# funkcja seek - chodzenie po znakach(przeskakujemy o tyle znakow
# do przodu ile podamy

# wczytywanie pojedyncznej linii, w nawiasie mozemy podac max limit znakow
print(f.readline())

# wczytywanie calosci pliku i skonwertowanie jej do tablicy linijek
print(f.readlines())

# readline i readlines mozemy wykorzystać przy petli for :)

f.close()