# Класс Стэксет хранит только уникальные элементы. Операция добавления должна выполняться за 0(1)
# вывести последний элемент и размер стэка

class StackSet:
    def __init__(self):
        self.stack = list()
        self.unique = set()

    def push(self, value):
        if value not in self.unique:
            self.stack.append(value)
            self.unique.add(value)

    def pop(self):
        value = self.stack.pop()
        self.unique.remove(value)
        return value

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.unique)


stack = StackSet()

stack.push(2)
stack.push(3)
stack.push(2)
stack.push(1)

print(stack.peek())
print(stack.size())
