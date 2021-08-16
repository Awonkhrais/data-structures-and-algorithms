class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack :
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node= Node(value)
        new_node.next = self.top  # assign the node that was previously the top node as the next of our new node
        self.top = new_node       # updates the top of our stack so it points to the new node

    def pop(self):
        current = self.top

        if self.is_empty():
           raise Exception('The stack is empty')
        else:
            self.top = self.top.next
            current.next = None
            return current.data

    def peek(self):

        if self.is_empty():
           raise Exception('The stack is empty')
        return self.top.data

    def is_empty(self):
        if self.top == None :
            return True
        return False


    def __str__(self):
        content=''
        current = self.top
        while current:
            content+= f"{{{str(current.data)}}} ->"
            current=current.next
        content+="Null"
        return content

    def max(self):
        max = Stack()
        max.push(0)
        current = self.top
        while current:
            if current.data > max.top.data:
                max.push(current.data)
            current=current.next
        return max.top.data
    

####################### Queue ##########################

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        new_node = Node(value)

        if self.is_empty():
            self.rear = new_node
            self.front = new_node
        else:
            new_node.next = self.rear
            self.rear = new_node

    def is_empty(self):

        if (not self.rear and self.front) or (self.rear and not self.front):
            raise Exception("Empty queue")
        return not self.rear

    def peek(self):
        if self.is_empty():
            raise Exception('The queue is empty')
        return self.front.data

    def dequeue(self):
        if self.front is None:
            raise Exception('empty queue')
        current = self.front
        self.front = self.front.next
        current.next = None
        return current.data

    def __str__(self):
        content=''
        current = self.rear
        content+="Null"
        while current:
            content+= f"-> {{{str(current.data)}}}"
            current=current.next
        return content





if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(30)
    stack.push(4)
    print(stack)
    print(stack)
    # stack.pop()
    # print(stack)
    # print(stack.is_empty())
    # print(stack.peek())

    # queue = Queue()
    # queue.enqueue(1)
    # queue.enqueue(12)
    # queue.enqueue(13)
    # queue.enqueue(13)
    # print(queue)
    # # print(queue.is_empty())
    # # print(queue.peek())
    # print(queue.dequeue())
    # print(queue)

