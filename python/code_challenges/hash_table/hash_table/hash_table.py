from linkedlist import *

class HashTable :

    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [None] *self.size
