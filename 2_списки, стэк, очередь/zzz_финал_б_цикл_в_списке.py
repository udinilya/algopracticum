# Написать функцию, которая определяет есть ли в связном списке цикл

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def has_cycle(node):
    values = []
    while node:
        values.append(node)
        if node.next in values:
            return True
        else:
            node = node.next
    return False


n3 = Node('wendsday')
n2 = Node('tuesday', n3)
n1 = Node('monday', n2)

print(has_cycle(n1))
