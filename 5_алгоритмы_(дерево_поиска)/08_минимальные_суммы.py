# Даны 2 массива, отсортированные по неубыванию, а также число k. Нужно определить k пар с наименьшей суммой.
# Пара должна состоять из одного элемента первого массива и одного элемента второго.

a = [1, 1, 2, 3]
b = [1, 2, 3, 4]
k = 7


def solution(a, b):
    pairs = [[(i, j), i+j] for i in a for j in b]

    pairs.sort(key=lambda x: x[1])

    for pair in pairs[:k]:
        print(*pair[0])


solution(a, b)
