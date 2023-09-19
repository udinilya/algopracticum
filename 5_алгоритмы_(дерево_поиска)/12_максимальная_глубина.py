# Функция должна вернуть число, равное максимальному числу узлов в ветке.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self . value)


def solution(node):
    levels = 0
    children = [node]
    children_next = []
    while children:
        levels += 1
        for child in children:
            if child.left:
                children_next.append(child.left)
            if child.right:
                children_next.append(child.right)

        children, children_next = children_next, []

    return levels


n6 = Node('5')
n5 = Node('12', n6)
n4 = Node('8')
n3 = Node('4')
n2 = Node('1', n4, n5)
n1 = Node('3', n2, n3)

print(solution(n1))
