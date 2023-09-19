# Дерево считается сбалансированным, если левое и правое поддеревья каждого узла
# отличаются по высоте не больше, чем на один.
# Вывести True если дерево считается сбалансированным

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
    children = [node]
    while children:
        for child in children:
            a = len(levels(child.left)) if child.left else 0
            b = len(levels(child.right)) if child.right else 0
            res = abs(a-b)
            if res > 1:
                return False

            if child.left:
                children.append(child.left)
            if child.right:
                children.append(child.right)

    return True

n8 = Node('9')
n7 = Node('8')
n6 = Node('4')
n5 = Node('7', n6, n7)
n4 = Node('5')
n3 = Node('3', n4)
n2 = Node('2', n3)
n1 = Node('0', n2, n5)
print(solution(n1))
