# Вывести максимум из элементов стэка
# Сложность операции должна быть О(1), поэтому встроенную функцию мксимума использовать нельзя


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_num = []

    def push(self, item):
        if not self.max_num or item >= self.max_num[-1]:
            self.max_num.append(item)
        elif item < self.max_num[-1]:
            self.max_num.append(self.max_num[-1])
        self.items.append(item)

    def pop(self):
        if not self.items:
            print('error')
        else:
            self.max_num.pop()
            self.items.pop()

    def get_max(self):
        if not self.items:
            print('None')
        else:
            print(self.max_num[-1])


stack = StackMaxEffective()

stack.pop()
stack.pop()
stack.push(3)
stack.push(-5)
stack.push(7)
stack.push(8)
stack.get_max()
stack.pop()
stack.pop()
stack.get_max()
