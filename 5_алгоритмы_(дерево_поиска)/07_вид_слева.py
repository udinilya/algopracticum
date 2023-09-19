# Функция должна вернуть список вершин дерева, которые видны, если к нему подойти слева.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self . value)


def levels(node):
    level_to_nodes = []
    children = [node]
    children_next = []
    while children:
        level_to_nodes.append([])
        for child in children:
            if child.left:
                children_next.append(child.left)
            if child.right:
                children_next.append(child.right)
            level_to_nodes[-1].append(child.value)

        children, children_next = children_next, []

    return level_to_nodes


def solution(node):
    first = []
    for level in levels(node):
        first.append(level[0])

    return first


n9 = Node('14')
n8 = Node('17')
n7 = Node('10', n9)
n6 = Node('8', n8)
n5 = Node('5')
n4 = Node('4')
n3 = Node('3', n6, n7)
n2 = Node('2', n4, n5)
n1 = Node('1', n2, n3)

print(solution(n1))
