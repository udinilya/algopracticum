# Создать функцию для определения правильной скобочной последовательности

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def is_correct_bracket_seq(stroka):
    stack = Stack()

    for i in stroka:
        opened_to_closed = {'(': ')', '[': ']', '{': '}'}
        if i in ('(', '[', '{'):
            stack.push(i)
        elif i in (')', ']', '}'):
            if not stack.items:
                return False
            j = stack.pop()
            if i != opened_to_closed[j]:
                return False

    if not stack.items:
        return True
    else:
        return False


print(is_correct_bracket_seq('[()]'))
