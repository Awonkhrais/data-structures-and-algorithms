# Stacks and Queues

- Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.

- Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.

## Challenge

- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

- Create a Stack class that has a top property. It creates an empty Stack when instantiated. This object should be aware of a default empty value assigned to top when the stack is created.

- Create a Queue class that has a front property. It creates an empty Queue when instantiated. This object should be aware of a default empty value assigned to front when the queue is created.

## Approach & Efficiency

My approch is descriped in my code: [code](./stack_and_queue/stack_and_queue.py)



## API

#### My stack and queue class has 4 methods:

- `pop()`: this method removes the item on top of the stack by setting its pointer to self.top.next.

- `push()` : This method pushes a new node into the stack by setting the current top node as the incoming node's next.

- `peek()` : This method returns the value at the top of the stack, if it exists

- `is_empty()`:  Checks if self.top exists and returns a boolean , for queue >> Checks if self.front exists and returns a boolean

- `enqueue()`: Appends a node to the end of the queue by pointing the current rear (if it exists) to the new node, and assigning self.rear to the new node.

- `dequeue()`: removes a node from the front of the queue.

