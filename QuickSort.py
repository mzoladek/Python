"""

Oto program, który pobiera ciąg napisów (zapisanych w jednej linii oddzielonych spacją) 
oraz sortuje dany ciąg rosnąco używając do tego metody sortowania QuickSort 

Do wyboru mamy jeden z poniższych wariantów sortowania QuickSort: 

 
1.odstawowy z podziałem skrajnie prawego elementu 

2.z medianą (czyli elementem środkowym co do wartości) z trzech następujących elementów tablicy:
skrajnie lewego (A[p]), środkowego (A[p + (r−p)/2]), skrajnie prawego (A[r]). 

3.Z wybranym pseudolosowo elementem podziału (RandomizedQuicksort); 

Dla prostoty zadania zakładamy, że ciągi te mają słowa tej samej długości. 

Należy tutaj odróżnić wielkość liter w danych słowach. Mają one być zachowane !!!. 

Sample Input 1:  

ala ada aaa  

Sample Output 1:  

aaa ada ala  

Sample Input 2:  

aaa ada ala  

Sample Output 2:  

aaa ada ala 
"""


import random


def sort(tab):

    if tab is None or len(tab) == 0:

        return

    n = len(tab)

    quicksort(tab, 0, n - 1)

    return tab


def quicksort(tab, lewy, prawy):

    if lewy >= prawy:

        return

    granica = partition(tab, lewy, prawy)

    if granica - lewy < prawy - granica:

        quicksort(tab, lewy, granica - 1)

        quicksort(tab, granica + 1, prawy)

    else:

        quicksort(tab, granica + 1, prawy)

        quicksort(tab, lewy, granica - 1)


def wybierz_pivot(tab, lewy, prawy):

    # right element

    # return tab[prawy]

    # middle element

    # srodkowy = int(lewy + (prawy - lewy) / 2)

    # pivot = tab[srodkowy]
    # tab[srodkowy], tab[prawy] = tab[prawy], tab[srodkowy]
    # return pivot

    # random element

    randpivot = random.randint(lewy, prawy)

    tab[randpivot], tab[prawy] = tab[prawy], tab[randpivot]

    return tab[prawy]


def partition(tab, lewy, prawy):

    pivot = wybierz_pivot(tab, lewy, prawy)

    granica = lewy - 1

    i = lewy

    while i < prawy:

        if tab[i] < pivot:
            granica += 1
            if granica != i:
                tab[granica], tab[i] = tab[i], tab[granica]
        i += 1

    granica += 1

    if granica != prawy:
        tab[granica], tab[prawy] = tab[prawy], tab[granica]

    return granica


slowa = input()
lista = slowa.split()

print(*sort(lista), sep=" ")
