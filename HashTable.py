# -*- coding: utf-8 -*-
"""
Oto program, który będzie realizował tablicę haszującą wraz z metodą łańcuchową 
gdzie będą wstawiane dane z pliku data.txt 
"""


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        hash = 0
        for ch in key:
            hash += ord(ch)
        return hash % self.size

    def insert(self, key, value):
        hash = self.hash_function(key)
        self.table[hash].append((key, value))

    def search(self, key):
        hash = self.hash_function(key)
        for k, v in self.table[hash]:
            if k == key:
                return v
        return None


def read_data(filename):
    with open(filename, 'r') as f:
        for line in f:
            key = line.strip()
            ht.insert(key, True)


ht = HashTable(4000)

read_data('data.txt')

keys = ['gcc', 'programmer', 'wasted']
for key in keys:
    print(f'{key}: {ht.search(key)}')
