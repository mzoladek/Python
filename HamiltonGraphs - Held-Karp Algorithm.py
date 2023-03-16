# -*- coding: utf-8 -*-
"""
Oto program, który sprawdza czy graf nieskierowany G 
podany przez użytkownika poprzez macierz sąsiedztwa jest:

Hamiltonowski
Półhamiltonowski
Niehamiltonowski
Niespójny

Dane testowe są grafami nieskierowanymi. Używyam tutaj algorytmu korzystającego z programowania dynamicznego.
Sample Input 1:

0 0 0 1
0 0 1 1
0 1 0 0
1 1 0 0

Sample Output 1:

Graf jest półhamiltonowski

Sample Input 2:

0 1 1 0
1 0 0 0
1 0 0 0
0 0 0 0

Sample Output 2:

Graf jest niespójny

Sample Input 3:

0 1 1 0 0 1
1 0 1 1 1 1
1 1 0 1 1 1
0 1 1 0 1 1
0 1 1 1 0 1
1 1 1 1 1 0

Sample Output 3:

Graf jest hamiltonowski

Sample Input 4:

0 0 0 0 0 1 1 1 0 1
0 0 1 1 0 0 0 0 0 0
0 1 0 0 0 0 0 0 1 1
0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0
1 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
1 0 1 0 0 0 1 0 0 0

Sample Output 4:

Graf nie jest hamiltonowski
"""


import numpy as np

def niespojny(graf):
    sprawdz = 1
    n = len(graf)
    visited = [0] * n
    visited[0] = 1

    def dfs(u):
        visited[u] = 1
        for v in range(n):
            if graf[u][v] == 1 and not visited[v]:
                dfs(v)

    dfs(0)
    for i in range(n):
        if (visited[i] == 0):
            sprawdz = 0
    return sprawdz

def k_sub(V, k):
    n = len(V)
    V = np.array(V)

    A = [i for i in range(k)]
    if n == k:
        return [tuple(V[A])]
    p = k - 1
    res = []
    while p >= 0:
        #        print(A)
        res.append(tuple(V[A]))
        if A[k - 1] == n - 1:
            p = p - 1
        else:
            p = k - 1
        if p >= 0:
            for i in range(k - 1, p - 1, -1):
                A[i] = A[p] + i - p + 1
    return res


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

c = np.array(array)
N = n

if niespojny(array) == 0:
    print("Graf jest niespójny")
    exit()

Vn = np.arange(N)
opts = [0 for i in range(N)]

# s = 2
for s in Vn:
    OPT = {}
    V = list(Vn)
    V_s = V[:s] + V[s + 1:]

    for v in V_s:
        OPT[(v, v)] = c[s, v]

    for j in range(2, N):
        Sbs = k_sub(V_s, j)
        for S in Sbs:
            for i in range(len(S)):
                v = S[i]
                S_v = S[:i] + S[i + 1:]
                os = []
                for u in S_v:
                    os.append(OPT[S_v + (u,)] + c[u, v])
                OPT[S + (v,)] = np.max(os)
    os = []
    for v in V_s:
        os.append(OPT[tuple(V_s) + (v,)] + c[v, s])
    opts[s] = np.max(os)


res = np.min(opts)

if res == N:
    print("Graf jest hamiltonowski")
elif res == N - 1:
    print("Graf jest półhamiltonowski")
elif res < N - 1:
    print("Graf nie jest hamiltonowski")




