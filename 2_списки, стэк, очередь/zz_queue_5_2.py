# Реализовать структуру данных Дэк, что бы все операции выполнялись за О(1)
# Реализовано с помощью двух отдельных списков, один это начало очереди и второй это конец очереди

class Deque:
    max_size = 6

    def __init__(self):
        self.back = [None] * Deque.max_size
        self.back_head = 0
        self.back_tail = 0
        self.front = [None] * Deque.max_size
        self.front_head = 0
        self.front_tail = 0
        self.size = 0

    def push_back(self, value):
        if self.size == Deque.max_size:
            print('error')
        else:
            self.back[self.back_tail] = value
            self.back_tail = (self.back_tail + 1) % Deque.max_size
            self.size += 1

    def push_front(self, value):
        if self.size == Deque.max_size:
            print('error')
        else:
            self.front[self.front_tail] = value
            self.front_tail = (self.front_tail + 1) % Deque.max_size
            self.size += 1

    def pop_back(self):
        if self.size == 0:
            print('error')
        else:
            if self.back[self.back_tail-1] is not None:
                value = self.back[self.back_tail-1]
                self.back[self.back_tail-1] = None
                self.back_tail = (self.back_tail - 1) % Deque.max_size
                self.size -= 1
                print(value)
            else:
                value = self.front[self.front_head]
                self.front[self.front_head] = None
                self.front_head = (self.front_head + 1) % Deque.max_size
                self.size -= 1
                print(value)

    def pop_front(self):
        if self.size == 0:
            print('error')
        else:
            if self.front[self.front_tail-1] is not None:
                value = self.front[self.front_tail-1]
                self.front[self.front_tail-1] = None
                self.front_tail = (self.front_tail - 1) % Deque.max_size
                self.size -= 1
                print(value)
            else:
                value = self.back[self.back_tail - 1]
                self.back[self.back_tail - 1] = None
                self.back_tail = (self.back_tail - 1) % Deque.max_size
                self.size -= 1
                print(value)


q = Deque()

q.push_front(201)
q.push_front(20)
q.push_front(10)
q.pop_back()
q.push_front(30)
q.push_front(40)
q.push_front(50)
q.pop_back()
q.push_front(60)
q.pop_back()
q.pop_front()


print(q.front)
print(q.back)