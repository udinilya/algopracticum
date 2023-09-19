# Помогите ребятам определить, является
# ли дерево, которое они нашли деревом - анаграммой?
# Дерево является анаграммой, если оно симметричное относительно своего центра.

# Сережино решение с использованием рекурсии

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self) :
        return str (self . value)


def is_symetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    if root1.value == root2.value:
        return is_symetric(root1.left, root2.right) and is_symetric(root1.right, root2.left)
    return False


def solution(node):
    return is_symetric(node, node)



n7 = Node('4')
n6 = Node('3')
n5 = Node('3')
n4 = Node('4')
n3 = Node('2', n6, n7)
n2 = Node('2', n4, n5)
n1 = Node('1', n2, n3)

print(solution(n1))
