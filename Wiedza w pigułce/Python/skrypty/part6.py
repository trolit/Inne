# ----------------------
# WLASNE MODULY
# IMPORT, FROM, AS
# ----------------------

# importujemy nasz zestaw funkcji
import foo

# uprzednio korzystalismy z modulu time

# modul - zestaw funkcji ktore mozemy
# dolaczyc do naszego projektu w razie
# gdybysmy potrzebowali z nich skorzystac
# sa jako modul gdyż właśnie nie musimy
# zawsze ich zawierać i dzieki temu nie
# zuzywamy niepotrzebnie zasobow komputera

# korzystamy z funkcji z modulu o nazwie foo
foo.test("\nCzesc, ta funkcja jest z modulu foo i nazywa sie test")

foo.apple("\nJablko")


# UWAGA:
# jak zaimportowac tylko jedna funkcje(aby nie importowac calego modulu)?
# po przecinku mozemy kilka funkcji importowac

from foo import test, apple

test("Jedna z funkcji zaimportowana")

# inny przyklad:
from time import sleep
# importujemy tylko funkcje sleep wiec za pomoca nazwy sleep sie tylko odwolujemy a nie time.sleep
# jakbysmy zaimportowali caly modul time :)

# przyklad:
sleep(1)

