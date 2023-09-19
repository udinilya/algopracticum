# Гуляя по вилле Кондратия, ребята нашли генеалогическое древо его семьи. Им стало интересно, сколько лет прожили члены семьи
# разных поколений. Вывести список подсписков с возрастами поколений


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return str(self . value)


def solution(node):
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


n6 = Node('21')
n5 = Node('17')
n4 = Node('32')
n3 = Node('54', n6)
n2 = Node('28', n4, n5)
n1 = Node('36', n2, n3)

print(solution(n1))
