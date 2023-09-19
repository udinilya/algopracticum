# Вывести индекс первого вхождения заданного элемента
# Если элемента в списке нет то выетсит -1

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, elem):
    index = -1
    while node:
        index += 1
        if node.value == elem:
            break
        node = node.next_item
    else:
        index = -1
    print(index)


n5 = Node('third')
n4 = Node('four', n5)
n3 = Node('third', n4)
n2 = Node('second', n3)
n1 = Node('first', n2)

solution(n1, 'third')
