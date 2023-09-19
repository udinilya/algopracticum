# Вывести значение корня из двух с точностью пять знаков
# Выводит не точное значение

k = 1
n = 2
z = 2


def solution(n, z, k):
    s = str(n)
    if abs(s.find('.') - len(s)) - 1 == 5:
        print(n)
    else:
        num = n * n
        if num > 2:
            z = n
            new = float((n + k) / 2)
            solution(new, z, k)
        elif num < 2:
            new = float((n + z) / 2)
            k = n
            solution(new, z, k)


solution(n, z, k)
