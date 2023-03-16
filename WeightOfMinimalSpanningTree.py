"""
Oto program, który wczytuje od użytkownika macierz sąsiedztwa,
a następnie wypisuje wagę najmniejszego drzewa spinającego tego grafu. 
W przypadku niespójnego grafu, program wypisuje komunikat: Graf nie jest spójny.

Sample Input:

0  0  6  0  0  0  0  0
0  0  0 10  0  0  0  6
6  0  0  9  0  0  0  0
0 10  9  0  0 10  2  0
0  0  0  0  0  0  1  0
0  0  0 10  0  0  7  0
0  0  0  2  1  7  0  8
0  6  0  0  0  0  8  0

Sample Output:

39
"""
def read_matrix():
    n = input()
    m = n.split()

    lista_elementow = []
    make_int = [int(x) for x in m]
    ilosc_wierzcholkow = len(make_int)
    lista_elementow.append(make_int)

    for i in range(0, len(make_int) - 1):
        a = input()
        b = a.split()
        make_int = [int(x) for x in b]
        lista_elementow.append(make_int)

    return lista_elementow, ilosc_wierzcholkow


def get_minimal_spannal_tree_wage(lista_elementow, ilosc_wierzcholkow):
    # Algorytm Prima

    selected = [False] * ilosc_wierzcholkow
    selected[0] = True
    suma = 0
    while True:
        minimum = float("inf")
        x = 0
        y = 0
        for i in range(ilosc_wierzcholkow):
            if selected[i]:
                for j in range(ilosc_wierzcholkow):
                    if (not selected[j]) and lista_elementow[i][j]:
                        if minimum > lista_elementow[i][j]:
                            minimum = lista_elementow[i][j]
                            x = i
                            y = j
        suma += minimum
        selected[y] = True
        if selected.count(True) == ilosc_wierzcholkow:
            print(suma)
            break
        elif minimum == float("inf"):
            print("Graf nie jest spójny")
            break



lista_elementow, ilosc_wierzcholkow = read_matrix()
get_minimal_spannal_tree_wage(lista_elementow, ilosc_wierzcholkow)
