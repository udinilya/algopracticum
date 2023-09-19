# Удалить из связного списка элемента с указанным индексом idx

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    head = node
    if idx != 0:
        while idx-1:
            node = node.next_item
            idx -= 1
        node.next_item = node.next_item.next_item
    else:
        head = head.next_item
    return head


def printer(node):
    while node:
        print(node.value)
        node = node.next_item


n4 = Node('four')
n3 = Node('third', n4)
n2 = Node('second', n3)
n1 = Node('first', n2)

printer(solution(n1, 0))
