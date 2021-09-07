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

####################### HashTable ######################

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


    def add(self,key,value):
        index = self.hash(key)
        if self._buckets[index] == None :
            self._buckets[index] = LinkedList()

        self._buckets[index].append([key,value])

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
