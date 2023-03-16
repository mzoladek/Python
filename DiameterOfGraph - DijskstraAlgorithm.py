"""
Średnicą grafu nazywamy największą odległość najkrótszych ścieżek, jaka występuje między wierzchołkami.
Oto program, który dla ważonej macierzy sąsiedztwa obliczy średnicę grafu.
Dla prostoty zakładamy, że grafy są spójne i jego wagi są dodatnie.

0 8 0 0 7
8 0 0 2 0
0 0 0 2 0
0 2 2 0 0
7 0 0 0 0

Sample Output 1:

19

Sample Input 2:

0 8 0 1
8 0 6 5
0 6 0 1
1 5 1 0

Sample Output 2:

6
"""


import sys

def dijkstra(n, array, start_vertex):
    vertices = []
    costs = []
    previous = []
    s = []

    for i in range(n):
        vertices.append(i)
        costs.append(sys.maxsize)
        previous.append(-1)
    costs[start_vertex] = 0

    while vertices:
    
        u = min(vertices, key=lambda vertex: costs[vertex])
        s.append(u)
        vertices.remove(u)

        for v, cost in enumerate(array[u]):
            if cost > 0 and v in vertices and costs[v] > costs[u] + cost:
                costs[v] = costs[u] + cost
                previous[v] = u
    return costs, previous

array = []
n = 0
while True:
    try:
        a = list(map(int, input().split()))
        if a == []:
            break
        array.append(a)
        n += 1
    except EOFError:
        break
    except:
        print("BŁĄD")
        exit()

array_len = len(array)
max_distance = 0

for i in range(array_len - 1):
    result = dijkstra(n, array, i)
    m = max(result[0])
    if max_distance < m:
        max_distance = m

print(max_distance)