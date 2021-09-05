import re
class Node:

    def __init__(self, value=""):
        self.value = value
        self.next = None

    def __add__(self, other):
        return Node(self.value + other.value)

    def __str__(self):
        return str(self.value)


class LinkedList():

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head

        self.head = node

    def includes(self,value):
        current=self.head
        while current :
            if value ==current.value[0]:
                return True
            current=current.next
        return False

    def append(self,value):
        new_node=Node(value)

        if self.head == None:
            self.head = new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node

class HashTable :

    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [None]*size


    def hash(self, key):
        '''
        Used to generate a memory location from the key
        '''
        sum= 0
        for char in key:
            sum += ord(char)
        hashed_key  = (sum * 19) % self.size
        return hashed_key


    def add(self,key):
        '''
        this function take a string key and a value then add them in the hashtable as a list
        '''
        index = self.hash(key)
        if self._buckets[index] is None:
            self._buckets[index] = key
            return None
        return key

    def get(self,key):

        index = self.hash(key)
        if self._buckets[index] == None:
            return None
        else:
            current=self._buckets[index].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

    def contains(self,key):

        index=self.hash(key)
        if self._buckets[index]:
            return self._buckets[index].includes(key)
        else:
            return False


    def word_repeated(self , string):
        if string == '':
            raise Exception("the string is empty")
        string = re.sub(r'[^\w\s]', '', string)
        strings = string.split(' ')
        for word in strings:
            if self.add(word):
                return word
        return 'No repeated words'


if __name__=='__main__':
    hash_map=HashTable()
    print(hash_map.first_repeated("Once upon a time, there was a brave princess who..."))

