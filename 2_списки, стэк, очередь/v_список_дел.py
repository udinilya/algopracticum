# Написать функцию, которая печатает список дел (связный список), на вход получая тоолько голову списка

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node):
    while node:
        print(node.value)
        node = node.next_item


n2 = Node('second')
n1 = Node('first', n2)

solution(n1)
