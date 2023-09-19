# Реализовать очередь на основе массива.
# Команда  pop удаляет и выводит удаленный элемент
# Команда peek выводит первый элемент массива

class MyQueue:
    def __init__(self):
        self.queue = list()

    def is_empty(self):
        return not self.queue

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if not self.queue:
            print('None')
        else:
            print(self.queue.pop(0))

    def peek(self):
        if not self.queue:
            print('None')
        else:
            print(self.queue[0])

    def size(self):
        print(len(self.queue))


q = MyQueue()

