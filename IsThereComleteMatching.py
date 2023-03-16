# -*- coding: utf-8 -*-
"""
Oto program, który dla podanego grafu dwudzielnego w postaci listy sąsiedztwa stwierdzi, czy istnieje skojarzenie całkowite 
oraz wyświetla to skojarzenie w danym grafie.

Sample Input 1:

1 5 8 9
2 5
3 7 8
4 6 8
5 1 2
6 4
7 3
8 1 3 4
9 1

Sample Output 1:

Istnieje skojarzenie doskonałe

Sample Input 2:

1 5
2 5
3 5 7 8 9
4 5 6 7 9
5 1 2 3 4
6 4
7 3 4
8 3
9 3 4

Sample Output 2:

Nie istnieje skojarzenie doskonałe

"""

def input_list():
    A = []
    while True:
        try:
            A.append(list(map(int, input().split(" "))))
        except:
            break
    return A


def change_partners(chosen, A, m):
    for i, j in chosen.items():

        if j == m:

            for k in A[i - 1][1:]:
                if k != j:

                    chosen[A[i - 1][0]] = -1
                    if k not in chosen.values():
                        chosen[A[i - 1][0]] = k
                        
                        return
                    else:
                        change_partners(chosen, A, j)
                        if k not in chosen.values():
                            chosen[A[i - 1][0]] = k
                            return


def maxmatch(A):
    chosen = {}
    stopper = len(A) // 2

    for i in range(len(A) // 2):
        if A[i][0] > A[i][1]:
            stopper = i
            break

        for j in A[i][1:]:

            if j not in chosen.values():

                chosen[A[i][0]] = j

                break
            else:

                change_partners(chosen, A, j)
                if j not in chosen.values():
                    chosen[A[i][0]] = j
              
                    break

    if -1 not in chosen.values() and stopper == len(chosen.values()):
        print("Istnieje skojarzenie doskonałe")
        for x in chosen.items():
           print(x)
    else:
        print("Nie istnieje skojarzenie doskonałe")


maxmatch(input_list())




