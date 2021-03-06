# o Algorytmie A*

Algorytm A* jest jednym z najbardziej popularnych sposobów przeliczania/obliczania najkrótszej trasy pomiędzy
dwoma zadanymi punktami. Bardzo często wykorzystuje się go w - grach aby np. AI obliczało najkrótszą trasę do 
podejścia do bohatera przez co inteligencja wroga wydaje nam się bardziej naturalna. 

![Error](https://github.com/trolit/Moje.dokumenty/blob/master/Algorytm%20A_star/images/example1.PNG)
Powyżej efekt implementacji algorytmu w oparciu o jeden z wymienionych artykułów.

Postanowiłem od 0 spróbować zaimplementować ten algorytm w oparciu o WinForms w programie Visual Studio :) 

Widok aplikacji(v0.5):
![Error](https://github.com/trolit/Moje.dokumenty/blob/master/Algorytm%20A_star/images/przyklad2_v0.5.PNG)

Na ten moment program potrafi bez problemu odnaleźć drogę jednak nie zawsze jest ona "najkrótsza" -
problemem jest taki sam wynik "H" dla każdej z płytek przez którą możemy przejść. Mając sytuacje przykładowo
jak na rysunku poniżej:

![Error](https://github.com/trolit/Moje.dokumenty/blob/master/Algorytm%20A_star/images/przyklad2_ex.PNG)

mamy wynik "H" 7 dla każdej płytki, górnej, dolnej i lewej - program pójdźie na tą płytkę, która została 
wzięta jako pierwsza w liście OpenList - potem porównywana jest z pozostałymi możliwymi no i skoro wszystkie
mają ten sam wynik to ta pierwsza zostanie jako "najmniejsza". Na ten moment możliwe ścieżki są sprawdzane
w kolejności:

- czy mogę w prawo?

- czy mogę w górę?

- czy mogę w dół?

- czy mogę w lewo?

zatem dla powyższego przykładu pójdziemy w górę z racji że w prawo nie możemy iść.. a góra jest "najwcześniejszym" 
do sprawdzenia warunkiem - pozostałe nie są wykonywane. Ten aspekt pozostał mi do rozwiązania :)


Źródła:
> [Idea algorytmu(dobry artykuł)](https://www.raywenderlich.com/3016-introduction-to-a-pathfinding)

> [Przyklad A* w C#](https://gigi.nullneuron.net/gigilabs/a-pathfinding-example-in-c/)

> [A* w Unity](https://www.youtube.com/watch?v=mZfyt03LDH4)

> [A* w Unity(2)](https://www.youtube.com/watch?v=Uwn_QFjbl1k)