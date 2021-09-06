class QueueNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        node = QueueNode(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise Exception('Method not allowed on empty queue.')
        node = self.front
        self.front = self.front.next
        return node.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise Exception('Method not allowed on empty queue.')
        return self.front.value

class Node :
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree :
    def __init__(self):
        self.root = None

    def pre_order(self):
        output = []

        try:
            if self.root == None :
                print('The tree is empty')

            else:

                def walk(root):

                    # nonlocal output

                    output.append(root.value)
                    # output += [root.value]
                    # print(root.value)

                    if root.left:
                        walk(root.left)

                    if root.right:
                        walk(root.right)
                walk(self.root)

                return output
        except:
            print("somethig went wrong check your function")


    def in_order(self):
        output = []

        try:
            if self.root == None :
                print('The tree is empty')

            else:

                def walk(root):


                    if root.left:
                        walk(root.left)

                    # nonlocal output

                    output.append(root.value)
                    # output += [root.value]
                    # print(root.value)

                    if root.right:
                        walk(root.right)
                walk(self.root)

                return output
        except:
            print("somethig went wrong check your function")

    def post_order(self):
        output = []

        try:
            if self.root == None :
                print('The tree is empty')

            else:

                def walk(root):


                    if root.left:
                        walk(root.left)

                    if root.right:
                        walk(root.right)

                    # nonlocal output
                    output.append(root.value)
                    # output += [root.value]
                    # print(root.value)

                walk(self.root)

                return output
        except:
            print("somethig went wrong check your function")

##################### Code 16 ########################

    def find_max_value(self):

        if self.root.value != None :
            self.max = self.root.value
        else :
            raise Exception ('The tree is empty')

        def walk(root):

            if self.max < root.value:
                self.max = root.value


            if root.left:
                walk(root.left)


            if root.right:
                walk(root.right)
        walk(self.root)
        return(self.max)

#################### Code 17 ######################

    def breadth_first(self):
        result = []
        queue = Queue()
        current = self.root
        if current == None:
            return 'Empty tree'

        queue.enqueue(current)

        while current:
            current = queue.dequeue()
            result.append(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
            if queue.is_empty():
                break

        return result

#################### Code 18 ######################


    def fizz_buzz_tree(self):
        root = self.root
        new_tree = BinaryTree()

        if not root :
            return "tree is empty"

        def check_fizz_buzz(node):
            if node % 3 == 0 and node % 5 == 0:
                return ('FizzBuzz')
            elif node % 3 == 0:
                return ('Fizz')
            elif node % 5 == 0:
                return ('Buzz')
            elif node % 3 != 0 and node % 5 != 0:
                return str(node)


        def walk(node):
            new_node = Node(check_fizz_buzz(node.value))
            if node.left:
                new_node.left = walk(node.left)
            if node.right:
                new_node.right = walk(node.right)
            return new_node

        new_tree.root = walk(root)

        return (new_tree)

class BinarySearchTree(BinaryTree):

    def add (self,value):

        if self.root == None :
            self.root = Node(value)

        else:
            node = self.root

            while True :
                if node.value > value :
                    if node.left == None:
                        node.left = Node(value)
                        print(node.left)
                        break
                    node = node.left
                else:
                    if node.right == None:
                        node.right = Node(value)
                        print(node.right)
                        break
                    node = node.right
    def contains(self, value):

        if self.root == None:
            return 'The Tree is empty'
        else:
            node = self.root
            while node:
                if node.value == value:
                    return True
                if node.value > value:
                    if not node.left:
                        return 'The value is not in the Tree'
                    node = node.left
                else:
                    if node.right == None:
                        return 'The value is nor in the Tree'
                    node = node.right


