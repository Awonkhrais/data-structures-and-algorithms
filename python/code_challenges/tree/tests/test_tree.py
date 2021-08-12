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


def test_version():
    assert __version__ == '0.1.0'
