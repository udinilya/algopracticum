# создать калькулятор для подсчета польской обратной нотации используя стэк

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def get_num(exp):
    stack = Stack()

    for i in exp:
        if i.isdigit():
            stack.push(i)
        else:
            elem = stack.pop()
            elem_prev = stack.pop()
            if i == '*':
                stack.push(int(elem_prev) * int(elem))
            elif i == '/':
                stack.push(int(int(elem_prev) / int(elem)))
            elif i == '+':
                stack.push(int(elem_prev) + int(elem))
            elif i == '-':
                stack.push(int(elem_prev) - int(elem))

    print(*stack.items)


get_num(map(str, input().split()))
