# -*- coding: utf-8 -*-
"""
Oto program, który będzie wypisuje długość najdłuższego wspólnego podciągu dwóch ciągów XX oraz YY
- stosując programowanie dynamiczne ze spamiętywaniem działającą w czasie O(nm). 

Sample Input:  

acba 
abba  

Sample Output:  

3 
"""


def lcs(X, Y):

    m = len(X)

    n = len(Y)

    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):

        for j in range(n + 1):

            if i == 0 or j == 0:

                L[i][j] = 0

            elif X[i - 1] == Y[j - 1]:

                L[i][j] = L[i - 1][j - 1] + 1

            else:

                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]


X = input().lower()

Y = input().lower()

print(lcs(X, Y))


#       Ø 	a 	b 	a 	a 	b 	b 	a 	a 	a

# Ø 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0

# b 	0 	0 	1 	1 	1 	1 	1 	1 	1 	1

# a 	0 	1 	1 	2 	2 	2 	2 	2 	2 	2

# b 	0 	1 	2 	2 	2 	3 	3 	3 	3 	3

# a 	0 	1 	2 	3 	3 	3 	3 	4 	4 	4

# b 	0 	1 	2 	3 	3 	4 	4 	4 	4 	4
