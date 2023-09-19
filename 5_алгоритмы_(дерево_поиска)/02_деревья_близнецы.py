# Евлампии на день рождения подарили два дерева. Кондратий сказал, что они совершенно одинаковые. Но, по мнению Евлампии, они
# отличаются. Функция должна вернуть True если деревья являются близнецами. Иначе - False.

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
    else:
        res += '0'
    if node.right:
        res += search(node.right)
    else:
        res += '0'
    return res


def solution(root1, root2):
    a = search(root1)
    b = search(root2)

    if a == b:
        return True
    else:
        return False


n6 = Node('3')
n5 = Node('2')
n4 = Node('1', None, n5)

n3 = Node('3')
n2 = Node('2')
n1 = Node('1', n2, None)

print(solution(n1, n4))
