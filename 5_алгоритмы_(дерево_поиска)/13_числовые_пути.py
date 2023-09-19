# Дано дерево, в узлах которого записаны цифры от 0 до 9. Таким образом, каждый путь от корня до
# листа содержит число, получившееся конкатенацией цифр пути. Нужно найти сумму всех таких чисел в дереве.
# Например путь 1-2-3 это 123
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self) :
        return str (self . value)


def get_paths(node):
    cur = str(node.value)
    res = []

    if not node.left and not node.right:
        return [cur]
    if node.left:
        res += [cur + tail for tail in get_paths(node.left)]
    if node.right:
        res += [cur + tail for tail in get_paths(node.right)]

    return res


def solution(node):
    paths = get_paths(node)
    return sum(map(int, paths))


n5 = Node('1')
n4 = Node('2')
n3 = Node('3', n4, n5)
n2 = Node('2')
n1 = Node('1', n2, n3)

print(solution(n1))
