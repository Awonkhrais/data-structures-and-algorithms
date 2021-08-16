from tree import __version__

from tree.trees import BinaryTree, Node, BinarySearchTree



def test_empty_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected

def test_single_node():
    tree = BinarySearchTree()
    tree.add(18)
    actual = tree.root.value
    expected = 18
    assert actual == expected

def test_add_left_right():
    tree = BinarySearchTree()
    tree.add(18)
    tree.add(21)
    tree.add(17)
    result = [tree.root.value , tree.root.left.value , tree.root.right.value]
    actual = result
    expected = [18 , 17 , 21]
    assert actual == expected

def test_pre_order():
    tree = BinarySearchTree()
    tree.add(18)
    tree.add(23)
    tree.add(11)
    tree.add(20)
    tree.add(6)
    tree.add(32)
    actual = tree.pre_order()
    excepted = [18, 11, 6, 23, 20, 32]
    assert actual == excepted


def test_in_order():
    tree = BinarySearchTree()
    tree.add(18)
    tree.add(23)
    tree.add(11)
    tree.add(20)
    tree.add(6)
    tree.add(32)
    actual = tree.in_order()
    excepted = [6, 11, 18, 20, 23, 32]
    assert actual == excepted


def test_post_order():
    tree = BinarySearchTree()
    tree.add(18)
    tree.add(23)
    tree.add(11)
    tree.add(20)
    tree.add(6)
    tree.add(32)
    actual = tree.post_order()
    excepted = [6, 11, 20, 32, 23, 18]
    assert actual == excepted


##################### Code 16 ########################

def test_max_value():
    tree = BinarySearchTree()
    tree.add(18)
    tree.add(23)
    tree.add(11)
    tree.add(20)
    tree.add(6)
    tree.add(32)
    assert tree.find_max_value() == 32

##################################################

def test_breadth_first():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    actual = tree.breadth_first()
    assert expected == actual


def test_version():
    assert __version__ == '0.1.0'
