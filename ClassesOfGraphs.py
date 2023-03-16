"""
Oto program, który pobiera od użytkownika liste sąsiedztwa grafu G 
(wierzchołki numerujemy od jedynki),
a następnie wyświetli następujące informacje (każda informacja w osobnej linii):

Ilość wierzchołków
Ilość krawędzi
Ciąg stopni (nieposortowane)
Średni stopień grafu
Informacja czy graf należy do podstawowych klas grafów w kolejności:
Graf pełny - W tym przypadku program ma wypisać komunikat: Jest to graf pełny
Cykl - W tym przypadku program ma wypisać komunikat: Jest to cykl
Ścieżka - W tym przypadku program ma wypisać komunikat: Jest to ścieżka
Drzewo - W tym przypadku program ma wypisać komunikat: Jest to drzewo
Hiperkostka - W tym przypadku program ma wypisać komunikat: Jest to hiperkostka
W przypadku braku klas program ma wypisać komunikat: Graf nie należy do żadnej z podstawowej klas
Sprawdzamy w podanej powyżej kolejności i wypisujemy każdy poprawny wynik. Zakładamy dla prostoty, że grafy są spójne, ale dopuszczamy wierzchołki izolowane.


Sample Input 1:

1 6 9 10
2 4 5 9
3 6
4 2 8
5 2 7 8 9
6 1 3 7 10
7 5 6 9
8 4 5
9 1 2 5 7
10 1 6

Sample Output 1:

Ilość wierzchołków: 10
Ilość krawędzi: 14
Stopnie wierzchołków: 3 3 1 2 4 4 3 2 4 2
Średni stopień: 2.8
Graf nie należy do żadnej z podstawowych klas
Sample Input 2:

1 2 3 4
2 1 3 4
3 1 2 4
4 1 2 3

Sample Output 2:

Ilość wierzchołków: 4
Ilość krawędzi: 6
Stopnie wierzchołków: 3 3 3 3
Średni stopień: 3
Jest to graf pełny
Sample Input 3:

1 2 3
2 1 4 5
3 1 6 7
4 2 8
5 2
6 3
7 3
8 4

Sample Output 3:

Ilość wierzchołków: 8
Ilość krawędzi: 7
Stopnie wierzchołków: 2 3 3 2 1 1 1 1
Średni stopień: 1.75
Jest to drzewo

Sample Input 4:

1 2
2 1 3
3 2 4
4 3 5
5 4 6
6 5 7
7 6 8
8 7

Sample Output 4:

Ilość wierzchołków: 8
Ilość krawędzi: 7
Stopnie wierzchołków: 1 2 2 2 2 2 2 1
Średni stopień: 1.75
Jest to ścieżka
Jest to drzewo

Sample Input 5:

1 3 4
2 3 4
3 1 2
4 1 2

Sample Output 5:

Ilość wierzchołków: 4
Ilość krawędzi: 4
Stopnie wierzchołków: 2 2 2 2
Średni stopień: 2
Jest to cykl
Jest to hiperkostka
"""
import math


def read_input():
    numbers = []
    while True:
            a = input()
            if a!="":
                numbers.append(a)
            else:
                break

    return numbers


def split_input(numbers):
    split_list = []
    for i in numbers:
        split = i.split()
        split_list.append(split)
    return split_list


def get_names(split_list):
    names_list = []
    for i in split_list:
        name = int(i[0])
        names_list.append(name)
        del i[0]
    return names_list


def get_int_list(split_list):
    new_list = [list(map(int, lst)) for lst in split_list]
    return new_list


def get_lista_stopni(new_list):
    lista_stopni = []

    for i in range(0, len(new_list)):
        lista_stopni.append(len(new_list[i]))

    return lista_stopni


def get_dlugosc(names_list):
    return len(names_list)


def count():
    czy_drzewo = False

    numbers = read_input()
    # print("numbers:", numbers)

    split_list = split_input(numbers)
    # print("split list::", split_list)

    names_list = get_names(split_list)
    # print("names list:", names_list)

    new_list = get_int_list(split_list)
    # print("new list:", new_list)

    dlugosc = get_dlugosc(names_list)
    # print("dlugosc:", dlugosc)

    lista_stopni = get_lista_stopni(new_list)
    # print("lista stopni:", lista_stopni)
    # print("")

    ilosc_wierzcholkow = dlugosc
    ilosc_krawedzi = int(sum(lista_stopni) / 2)

    sredni_stopien = sum(lista_stopni) / ilosc_wierzcholkow

    if ilosc_wierzcholkow - 1 == ilosc_krawedzi and 0 not in lista_stopni:
        czy_drzewo = True

    return ilosc_wierzcholkow, ilosc_krawedzi, sredni_stopien, lista_stopni, czy_drzewo


def czy_pelny(lista_stopni):
    for i in lista_stopni:
        if i != len(lista_stopni) - 1:
            return False
    return True


def czy_cykl(lista_stopni):
    for i in lista_stopni:
        if i != 2:
            return False
    return True


def czy_sciezka(lista_stopni):
    if lista_stopni[0] == 1 and lista_stopni[-1] == 1:
        for n in lista_stopni[1:-1]:
            if n != 2:
                return False
    else:
        return False
    return True


def czy_hiperkostka(lista_stopni, ilosc_krawedzi):
    n = math.log(len(lista_stopni), 2)

    if ilosc_krawedzi == n * 2 ** (n - 1) and n.is_integer():
        return True
    else:
        return False


def write():
    ilosc_wierzcholkow, ilosc_krawedzi, sredni_stopien, lista_stopni, czy_drzewo = count()

    klasa = False

    print("Ilość wierzchołków:", ilosc_wierzcholkow)
    print("Ilość krawędzi:", ilosc_krawedzi)
    print("Stopnie wierzchołków:", ' '.join(map(str, lista_stopni)))
    if sredni_stopien.is_integer():
        print("Średni stopień:", int(sredni_stopien))
    else:
        print("Średni stopień:", sredni_stopien)

    if czy_pelny(lista_stopni):
        print("Jest to graf pełny")
        klasa = True
    if czy_cykl(lista_stopni):
        print("Jest to cykl")
        klasa = True
    if czy_sciezka(lista_stopni):
        print("Jest to ścieżka")
        klasa = True
    if czy_drzewo:
        print("Jest to drzewo")
        klasa = True
    if czy_hiperkostka(lista_stopni, ilosc_krawedzi):
        print("Jest to hiperkostka")
        klasa = True
    if not klasa:
        print("Graf nie należy do żadnej z podstawowych klas")


def main():
    write()


main()