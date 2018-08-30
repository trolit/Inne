# importujemy modul time
import time
# modul do obslugi dnia, tygodni, miesiecy itd..
import datetime

# -------------------------
#       DATA I CZAS
# -------------------------

print("Aktualizacja oprogramowania - prosze czekać!")

#uspienie programu na dwie sekundy
time.sleep(1)

print("Zakonczono aktualizacje oprogramowania!")

# ile czasu minelo od momentu zatrzymania programu
# jak to sprawdzić? - przyklady:
timer = time.time()
time.sleep(1)
elapsed = time.time()-timer

print("Minely: ", elapsed, " sekundy")

# modul ma taka sama nazwe jak obiekt dlatego piszemy datetime.datetime
# i mozemy sobie jakas gotowac funkcje wykorzystac
teraz = datetime.datetime.now()

print("Informacje o dacie: ", teraz)

# a jak tylko jedna rzecz wypisac?
# np. godziny i minuty, tylko trzeba
# by przekonwertowac liczby do napisu
# aby print mogl to obsluzyć

print(str(teraz.hour)+":"+str(teraz.minute))

# albo mozemy gotowa funkcje wykorzystac czyli strftime
# i podać w cudzysłowiu co chcemy aby funkcja zwróciła
# Dostaniemy ten sam efekt jak powyzej

print(teraz.strftime("%H:%M"))