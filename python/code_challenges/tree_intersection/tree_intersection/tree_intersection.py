from tree import *


def tree_intersection(tree1,tree2):

    if (tree1.root == None):
        return 'Tree1 is empty'
    if (tree2.root == None):
        return 'Tree2 is empty'
    else:
        common_list  = []
        list1 = tree1.in_order()
        list2 = tree2.in_order()
        for i in list1:
            if i in list2:
                common_list .append(i)

        if len(common_list ) != 0:
            return common_list
        else:
            return 'These trees does not have common values'


if __name__ == '__main__':
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()

    tree1.add(4)
    tree1.add(2)
    tree1.add(8)
    tree1.add(21)
    tree1.add(55)
    tree1.add(5)

    tree2.add(2)
    tree2.add(1)
    tree2.add(21)
    tree2.add(55)
    tree2.add(1)
    tree2.add(4)

    print(tree_intersection(tree1, tree2))
