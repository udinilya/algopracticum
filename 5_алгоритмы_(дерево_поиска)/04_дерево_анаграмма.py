# Помогите ребятам определить, является
# ли дерево, которое они нашли деревом - анаграммой?
# Дерево является анаграммой, если оно симметричное относительно своего центра.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self) :
        return str (self . value)


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
    print(levels(node)[1:])
    for level in levels(node)[1:]:
        if len(level) % 2 != 0:
            return False

        idx = len(level)//2
        if level[:idx] != list(reversed(level[idx:])):
            return False

    return True


n7 = Node('4')
n6 = Node('3')
n5 = Node('3')
n4 = Node('4')
n3 = Node('2', n6, n7)
n2 = Node('2', n4, n5)
n1 = Node('1', n2, n3)

print(solution(n1))
