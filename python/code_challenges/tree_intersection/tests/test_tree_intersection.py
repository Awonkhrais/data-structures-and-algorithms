from tree_intersection import __version__
from tree_intersection.tree import *
from tree_intersection.tree_intersection import tree_intersection


def test_version():
    assert __version__ == '0.1.0'

def test_common_trees():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    tree1.add(4)
    tree1.add(2)
    tree1.add(5)

    tree2.add(2)
    tree2.add(1)
    tree2.add(4)

    actual = tree_intersection(tree1, tree2)
    expected = [2, 4]
    assert actual == expected

def test_uncommon_trees():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    tree1.add(4)
    tree1.add(2)
    tree1.add(5)

    tree2.add(3)
    tree2.add(1)
    tree2.add(7)

    actual = tree_intersection(tree1, tree2)
    expected = 'These trees does not have common values'
    assert actual == expected
