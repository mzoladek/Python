# -*- coding: utf-8 -*-
"""
Oto program, który wczytuje od użytkownika tekst oraz dokonuje na podstawie podanego tekstu kod Huffmana,
wyświetla go, a następnie liczy ilość zaoszczędzonego miejsca dokonanego podczas kompresji tekstu za pomocą tego kodowania. 
"""

from queue import PriorityQueue


class Node:

    value = 0

    right = None

    left = None

    character = ""

    def isLeaf(self):

        return self.character != ""

    def __init__(self, val, ch):

        self.value = val

        self.character = ch

    def __lt__(self, other):

        if self.value != other.value:

            return self.value < other.value

        if not self.isLeaf() and other.isLeaf():

            return True

        if self.isLeaf() and not other.isLeaf():

            return False

        if self.isLeaf() and other.isLeaf():

            return ord(self.character[0]) < ord(other.character[0])

        return True


def createTree(text):

    occurences = {}

    for c in text:

        if occurences.__contains__(c):

            occurences[c] += 1

        else:

            occurences[c] = 1

    nodes = PriorityQueue()

    for c in occurences.keys():

        node = Node(occurences[c], c)

        nodes.put(node)

    nodeRoot = None

    while nodes.qsize() > 1:

        n1 = nodes.get()  #

        n2 = nodes.get()

        if n1.value == n2.value and not n1.isLeaf():

            pom = n1

            n1 = n2

            n2 = pom

        parent = Node(n1.value + n2.value, "")

        nodeRoot = parent

        parent.left = n1

        parent.right = n2

        nodes.put(parent)

    print("Słownik wystąpień: ")

    for key, value in occurences.items():

        print("'" + key + "': " + str(value) + ",", end=" ")

    print('\n')

    return nodeRoot


def encodeValues(n, str, txt):

    if n is None:

        return txt

    if n.isLeaf():

        print(n.character + " : " + str)

        txt = txt.replace(n.character, str)

    txt = encodeValues(n.left, str + "0", txt)

    txt = encodeValues(n.right, str + "1", txt)

    return txt


def decode(root, text):

    decoded = ""

    currNode = root

    for char in text:

        if char == '0':

            if currNode.left.isLeaf():

                decoded += currNode.left.character

                currNode = root

            else:

                currNode = currNode.left

        else:

            if currNode.right.isLeaf():

                decoded += currNode.right.character

                currNode = root

            else:

                currNode = currNode.right  #

    return decoded


#word = "abracadabra"
word = input(
    "Kodowanie Huffmana. Podaj tekst, który chcesz zakodować:").rstrip()

start_word = word

rootNode = createTree(word)

print("Oto tablica kodowania:")


word = encodeValues(rootNode, "", word)

print("Oto tekst po zakodowaniu: " + word)


encoded_text_size = len(word)


word = decode(rootNode, word)

print("Oto odkodowany tekst: " + word)


original_text_size = len(start_word) * 8

print("Zaoszczędzone miejsce: ", original_text_size - encoded_text_size, " bitów")
