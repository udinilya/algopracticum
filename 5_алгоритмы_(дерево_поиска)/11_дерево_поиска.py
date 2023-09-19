# написать функцию, которая определяет, является ли заданное дерево деревом поиска.
# Значения в левом поддереве должны быть строго меньше, в правом - строго больше значения в узле.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self) :
        return str (self . value)


def is_bst(node, less='inf', larger='-inf'):
    if not node:
        return True
    if node.value <= larger or node.value >= less:
        return False
    return is_bst(node.left, min(less, node.value), larger) and is_bst(node.right, less, max(node.value, larger))


n5 = Node('4')
n4 = Node('1')
n3 = Node('8')
n2 = Node('3', n4, n5)
n1 = Node('5', n2, n3)

print(is_bst(n1))
