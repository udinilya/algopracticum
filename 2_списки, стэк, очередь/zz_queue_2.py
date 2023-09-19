# Очередь принимает на вход параметр, ограничивающий количество элементов
# Очередь реализована с помощью массива.
# За счет того, что не нужно выделять каждый раз память выполняется за О(1)

class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None for _ in range(max_size)]
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.current_size = 0

    def push(self, value):
        if self.current_size != self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.current_size += 1
        else:
            print('error')

    def pop(self):
        if not self.queue:
            print('None')
        else:
            value = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.current_size -= 1
            print(value)

    def peek(self):
        if not self.queue:
            print('None')
        else:
            print(self.queue[self.head])

    def size(self):
        print(self.current_size)


q = MyQueueSized(3)
q.peek()
q.push(5)
q.push(2)
q.peek()
q.size()
q.size()
q.push(1)
q.size()
