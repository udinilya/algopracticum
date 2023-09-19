class Node:
    def __init__(self, value, next_item=None, prev=None):
        self.value = value
        self.next_item = next_item
        self.prev = prev


def solution(node):
    while node.next_item:
        node = node.next_item

    new_node = Node(node.value)
    node = node.prev
    while node:
        next_node = Node(node.value, None, new_node)
        new_node.next_item = next_node
        new_node = new_node.next_item
        node = node.prev
    while new_node.prev:
        new_node = new_node.prev

    return new_node


def printer(node):
    while node:
        print(node.value)
        node = node.next_item


n4 = Node('four')
n3 = Node('third', n4)
n2 = Node('second', n3)
n1 = Node('first', n2)
n4.prev = n3
n3.prev = n2
n2.prev = n1


printer(solution(n1))
