using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace przyklad1
{
    // klasa która będzie przechowywać wszelkie współrzędne bloków(płytek)
    class Location
    {
        public int X;
        public int Y;
        // oprócz współrzędnych X,Y każde "pole" będzie miało 3 wartości: F , G , H
        // G - odległość od punktu startowego
        // H - odległość do punktu docelowego
        // F - wynik sumy G+H
        public int F;
        public int G;
        public int H;

        // właściwość(property) "Parent" będzie przechowywać wartości poprzedniego "bloku" na którym
        // się znajdowaliśmy - - - - - - -  będzie pilnować czy osiągnęliśmy już nasz punkt docelowy
        public Location Parent;
    }

    class Program
    {
        // aby obliczyć wartość H:
        // H jest to pozioma i pionowa odległość do celu od miejsca w którym
        // obecnie się znajdujemy(ignoruje oczywiście przeszkody)
        static int ComputeHScore(int x, int y, int targetX, int targetY)
        {
            return Math.Abs(targetX - x) + Math.Abs(targetY - y);
        }

        // funkcja która proponuje kolejne bloki(płytki) przez jakie 
        // możemy przejść
        static List<Location> GetWalkableAdjacentSquares(int x, int y, string[] map)
        {
            var proposedLocations = new List<Location>()
            {
                new Location { X = x, Y = y - 1 },
                new Location { X = x, Y = y + 1 },
                new Location { X = x - 1, Y = y },
                new Location { X = x + 1, Y = y },
            };
                return proposedLocations.Where(
                l => map[l.Y][l.X] == ' ' || map[l.Y][l.X] == 'B').ToList();
        }

        static void Main(string[] args)
        {
            // inicjalizujemy algorytm wartościami:
            Location current = null;                            // obecna pozycja - null
            var start = new Location { X = 1, Y = 2 };          // miejsce w którym zaczynamy
            var target = new Location { X = 2, Y = 5 };         // miejsce do którego chcemy dotrzeć
            var openList = new List<Location>();                // lista miejsc w których nie byliśmy
            var closedList = new List<Location>();              // lista miejsc które już odwiedziliśmy

            // zmienna g to nic innego jak G czyli dystans(odległość) od punktu
            // w którym rozpoczęliśmy algorytm do punktu w którym obecnie się 
            // znajdujemy. Gdy będziemy się przemieszczać na kolejny "blok" to
            // zostanie po prostu zinkrementowana(g++)
            int g = 0;

            // algorytm rozpoczynamy dodając do naszej listy punkt w którym zaczynamy
            // po pierwszej iteracji(czyli przejściu na kolejny "blok" trafi on 
            // oczywiście do listy closedList)
            openList.Add(start);

            // zdefiniujmy sobie wygląd naszej planszy:
            string[] map = new string[]
            {
                "+-------+",
                "|       |",
                "|A X    |",
                "|XXX    |",
                "|   XX  |",
                "| B     |",
                "|       |",
                "+-------+",
            };
            // umówmy się, że najkrótsza droga musi zostać znaleziona od punktu B do punktu A
            // tam gdzie postawiliśmy znak X oznacza, że jest przeszkoda i nie można przez 
            // nią przejść

            // narysujmy na ekranie naszą planszę:
            // żeby widzieć jak się porusza algorytm
            for(int i = 0; i < map.Length; i++)
            {
                Console.WriteLine(map[i]);
            }

            // odczekajmy chwile
            Thread.Sleep(2000);

            // rdzeń algorytmu - to tutaj odbywa się większość operacji
            while (openList.Count > 0)
            {
                // za każdą iteracją algorytm A* otrzyma informację
                // o wartości zmiennej F czyli ile jeszcze drogi
                // ma do pokonania
                var lowest = openList.Min(l => l.F);
                current = openList.First(l => l.F == lowest);

                // obecny blok na którym się znajdujemy dodajemy do listy zamkniętej
                closedList.Add(current);

                // usuwamy obecny blok z listy "możliwe do zwiedzenia"
                openList.Remove(current);

                // mamy dwa warunki które pozwalają algorytmowi A* na zakończenie działania
                // 1. nie ma więcej bloków/kratek w openList do przetworzenia, które mogłyby
                // wskazywać na to, że nie ma ścieżki pomiędzy punktami A i B(ale tego tutaj 
                // nie zaimplementowano)

                // 2. poniższy warunek czyli, gdy ścieżka została znaleźiona i jest przez
                // algorytm "obsłużona"
                if (closedList.FirstOrDefault(l => l.X == target.X && l.Y == target.Y) != null)
                    break;
                
                // poniższa część algorytmu odpowiada za ocenianie sąsiednich bloków(płytek)
                var adjacentSquares = GetWalkableAdjacentSquares(current.X, current.Y, map);
                g++;

                // mamy teraz pętle która odpowiada za przeliczanie wartości sąsiednich płytek
                // (bloków) i dodawanie ich do listy openList jeżeli jest sens przejścia przez 
                // ten blok
                foreach (var adjacentSquare in adjacentSquares)
                {
                    // jeżeli ta płyka/blok jest już w closedList - nic dla niej nie rób
                    // - zignoruj
                    if (closedList.FirstOrDefault(l => l.X == adjacentSquare.X
                            && l.Y == adjacentSquare.Y) != null)
                        continue;

                    // jeżeli blok nie jest w liście openList
                    if (openList.FirstOrDefault(l => l.X == adjacentSquare.X
                            && l.Y == adjacentSquare.Y) == null)
                    {
                        // przelicz wartości dla bloku, ustaw rodzica
                        adjacentSquare.G = g;
                        adjacentSquare.H = ComputeHScore(adjacentSquare.X,
                            adjacentSquare.Y, target.X, target.Y);
                        adjacentSquare.F = adjacentSquare.G + adjacentSquare.H;
                        adjacentSquare.Parent = current;

                        // dodaj blok do listy openList
                        openList.Insert(0, adjacentSquare);
                    }
                    else
                    {
                        // sprawdzanie: jeżeli używając obecnej wartości G sprawia, że sąsiednie 
                        // bloki F mają mniejsze wartości to jeżeli tak - zaktualizuj(zmień) rodzica
                        // ponieważ to oznacza, że jest to lepsza,krótsza ścieżka
                        if (g + adjacentSquare.H < adjacentSquare.F)
                        {
                            adjacentSquare.G = g;
                            adjacentSquare.F = adjacentSquare.G + adjacentSquare.H;
                            adjacentSquare.Parent = current;
                        }
                    }
                }
            }

            // zakładając, że ścieżkę odnaleźiono, pokażmy ją
            while (current != null)
            {
                Console.SetCursorPosition(current.X, current.Y);
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.Write('_');
                Console.ForegroundColor = ConsoleColor.White;
                Console.SetCursorPosition(current.X, current.Y);
                current = current.Parent;
                System.Threading.Thread.Sleep(1000);
            }

            Console.SetCursorPosition(15, 9);
            Console.Write("\nKoniec działania algorytmu A*...\n<<naciśnij dowolny klawisz aby zakończyć>>\n");
            Console.ReadLine();
        }
    }
}
