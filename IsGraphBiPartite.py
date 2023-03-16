# -*- coding: utf-8 -*-
"""
Oto program, który pobiera nieskierowany graf spójny podany jako lista sąsiedztwa,
a następnie sprawdza, czy dany graf jest dwudzielny. 
Jeżeli graf jest dwudzielny, to program ma wypisać partycje dwudzielności (uporządkowane rosnąco) tego grafu.

Zakładamy, że zawsze wypisujemy najpierw mniejszą z partycji grafu dwudzielnego.

Sample Input 1:

1 4 5 6 7
2 4 5 6 7
3 4 5 6 7
4 1 2 3
5 1 2 3
6 1 2 3
7 1 2 3

Sample Output 1:

Graf jest dwudzielny
Pierwsza partycja: 1 2 3
Druga partycja: 4 5 6 7
Sample Input 2:

1 2 5
2 1 3
3 2 4
4 3 5
5 1 4

Sample Output 2:

Graf nie jest dwudzielny

"""

def dwudzielny_i_partycje(graf):
    kolory = {}
    kolejka = []
    for wierzcholek in graf:
        if wierzcholek not in kolory:
            kolory[wierzcholek] = 1
            kolejka.append(wierzcholek)
            while kolejka:
                obecny_wierzcholek = kolejka.pop(0)
                for sasiad in graf[obecny_wierzcholek]:
                    if sasiad not in kolory:
                        kolory[sasiad] = 1 - kolory[obecny_wierzcholek]
                        kolejka.append(sasiad)
                    elif kolory[sasiad] == kolory[obecny_wierzcholek]:
                        return False
    pierwsza_partycja = []
    druga_partycja = []
    for wierzcholek in kolory:
        if kolory[wierzcholek] == 1:
            pierwsza_partycja.append(wierzcholek)
        else:
            druga_partycja.append(wierzcholek)
    pierwsza_partycja.sort()
    druga_partycja.sort()
    return (True, (pierwsza_partycja, druga_partycja))

graf = {}
while True:
    try:
        linia = input()
        if linia == "":
            break
    except EOFError:
        break
    wierzcholek, *sasiedzi = linia.split()
    wierzcholek = int(wierzcholek)
    sasiedzi = [int(sasiad) for sasiad in sasiedzi]
    graf[wierzcholek] = sasiedzi

result = dwudzielny_i_partycje(graf)
if result:
    print("Graf jest dwudzielny")
    pierwsza_partycja, druga_partycja = result[1]
    if len(druga_partycja) < len(pierwsza_partycja):
        pierwsza_partycja, druga_partycja = druga_partycja, pierwsza_partycja
    print("Pierwsza partycja: ", end="")
    print(*pierwsza_partycja, sep=" ")
    print("Druga partycja: ", end="")
    print(*druga_partycja, sep=" ")
else:
    print("Graf nie jest dwudzielny")


