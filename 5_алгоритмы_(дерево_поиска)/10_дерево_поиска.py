# написать функцию, которая определяет, является ли заданное дерево деревом поиска.
# Значения в левом поддереве должны быть строго меньше, в правом - строго больше значения в узле.

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
    children = [node]
    while children:
        for child in children:
            if child.left:
                for elem in search(child.left):
                    if elem >= int(child.value):
                        return False
            if child.right:
                for elem in search(child.right):
                    if elem <= int(child.value):
                        return False

            if child.left:
                children.append(child.left)
            if child.right:
                children.append(child.right)

        return True


n5 = Node('5')
n4 = Node('1')
n3 = Node('8')
n2 = Node('3', n4, n5)
n1 = Node('5', n2, n3)

print(solution(n1))
