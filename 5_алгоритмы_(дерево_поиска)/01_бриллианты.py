# У Евлампии есть брошь с бриллиантами в виде дерева. В каждом узле дерева есть какое-то количество бриллиантов. Помогите
# выяснить, какое максимальное количество бриллиантов есть в одном узле.
# Задача на дерево поиска

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self) :
        return str (self . value)


def search(node):
    res = [int(node.value)]
    if node.left:
        res += search(node.left)
    if node.right:
        res += search(node.right)
    return res


def solution(node):
    return max(search(node))


n10 = Node('10')
n8 = Node('8')
n5 = Node('5')
n3_1 = Node('3', n8, n10)
n_beg = Node('1', n3_1, n5)

print(solution(n_beg))
