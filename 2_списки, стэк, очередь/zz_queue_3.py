# Необходимо вывести количество возможных анаграмм заданного шаблона
# Задано слово и шаблон

class MyQueue:
    def __init__(self):
        self.queue = list()

    def push(self, value):
        self.queue.append(value)


def anagram(word, pattern):
    q = MyQueue()
    count = 0
    sort_pattern = sorted(pattern)

    for j in range(0, len(word)):
        q.push(word[j: j+len(pattern)])

    for i in q.queue:
        if sorted(i) == sort_pattern:
            count += 1

    print(count)


anagram('abcsdabca', 'abc')
