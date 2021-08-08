from for_import import Stack,Node

class Pseudo_queue:
    def __init__(self):
        self.first_stack = Stack()
        self.reverse_stack = Stack()

    def enqueue(self,value):
        self.first_stack.push(value)
        return self.first_stack


    def dequeue(self):

        while self.first_stack.top :

            popped = self.first_stack.pop()

            self.reverse_stack.push(popped)

        self.reverse_stack.pop()

        while self.reverse_stack.top:

            self.first_stack.push(self.reverse_stack.pop())

        return self.first_stack








if __name__ == "__main__":
    pq = Pseudo_queue()
    pq.enqueue(7)
    pq.enqueue(5)
    print(pq.enqueue(3))
    print(pq.dequeue())


