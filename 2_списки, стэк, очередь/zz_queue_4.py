# Реализовать очередь на связном списке

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def solution(node):
    while node:
        print(node.value)
        node = node.next


class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def put(self, value):
        node = Node(value)
        if not self.tail:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.count += 1

    def get(self):
        if not self.head:
            print('error')
        else:
            elem = self.head
            self.head = self.head.next
            self.count -= 1
            print(elem.value)
            return elem.value

    def size(self):
        print(self.count)


q = MyQueue()

q.put(34)
q.put(23)
q.put(18)
q.get()
q.get()
