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


if __name__ == "__main__":
    # bt = BinaryTree()
    # bt.root = Node(18)
    # bt.root.right = Node(23)
    # bt.root.left = Node(11)
    # bt.root.right.left = Node(20)
    # bt.root.left.left = Node(6)
    # bt.root.right.right = Node(32)
    # # bst = BinarySearchTree()
    # # bst.root = Node(18)
    # # bst.root.right = Node(23)
    # # bst.root.left = Node(11)
    # # bst.root.right.left = Node(20)
    # # bst.root.left.left = Node(6)
    # # bst.root.right.right = Node(32)
    # # bst.add(13)
    # # bst.contains(18)
    # # print(bst.pre_order())
    # # print(bt.in_order())
    # # print(bt.post_order())
    # # print(bt.find_max_value())
    # print(bt.breadth_first())
    tree = BinarySearchTree()

    tree.add(5)
    tree.add(10)
    tree.add(15)
    tree.add(20)
    tree.add(25)
    tree.add(30)
    tree.add(35)
    tree.add(40)
    tree.add(45)


    print(tree.breadth_first())
