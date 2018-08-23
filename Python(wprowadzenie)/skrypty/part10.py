# ---------------------------------
#  DZIEDZICZENIE KLAS
# ---------------------------------
# + lepsza organizacja kodu
# + ograniczenie powtarzalnosci kodu

class Parent():

    def __init__(self):
        print("Klasa Parent, metoda init")

    def parent(self):
        print("Parent, Parent")

    def poke(self):
        print("Parent poked")

# klasa dziecko - dziedziczymy z Parent
class Child(Parent):

    def __init__(self):
        # przez super wywolujemy metode init od "rodzica" czyli klasy z ktorej dziedziczymy
        super().__init__()
        print("Klasa Child, metoda init")

    def poke(self):
        super().poke()
        print("Child poked")

# tworzymy obiekt klasy Child
child = Child()

child.poke()

# --------------------------------------------
# TWORZENIE WLASNYCH WYJATKOW
# --------------------------------------------

class TooColdException(Exception):
    # slowko pass - nic ono nie robi , zajmuje miejsce po prostu
    pass

    def __init__(self):
        super().__init__("Temperature is below absolute zero!")

def celsius_to_kelvin(temp):
    if temp < -273.15:
        # raise powoduje wywołanie wyjątku
        raise TooColdException()
    return temp + 273.15

print(celsius_to_kelvin(-300))



