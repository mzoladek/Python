"""
Oto program, który pobiera od użytkownika macierz sąsiedztwa, a następnie wyświetla informację o tym czy graf jest skierowany czy nie.

Sample Input 1:

0 0 0 1 1
0 0 0 0 0
0 0 0 0 1
1 0 0 0 1
1 0 1 1 0

Sample Output 1:

Graf jest nieskierowany

Sample Input 2:

0 0 0 1 0
0 0 0 1 1
0 0 0 1 1
0 0 0 0 0
1 0 0 1 0

Sample Output 2:

Graf jest skierowany

"""
n = input()
m = n.split()

skierowany = False

lista_elementow = []

make_int = [int(x) for x in m]

lista_elementow.append(make_int)

for i in range(0, len(make_int) - 1):
    a = input()
    b = a.split()

    make_int = [int(x) for x in b]

    lista_elementow.append(make_int)


for i in range(0, len(lista_elementow)):
    for j in range(0, len(lista_elementow)):
        if lista_elementow[i][j] != lista_elementow[j][i]:
            skierowany = True
            break
        else:
            continue

if skierowany:
    print("Graf jest skierowany")
else:
    print("Graf jest nieskierowany")
