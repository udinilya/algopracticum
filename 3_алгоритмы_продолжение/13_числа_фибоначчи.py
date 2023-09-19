# Нужно вывести n-ное число Фибоначчи
# Реализовано с рекурсией
# благодаря словарю не производим каждый раз вычисление значения, а берем из словаря, экономия времени

fib = {0: 1, 1: 1}


def solution(n):
    if n not in fib:
        fib[n] = solution(n-1) + solution(n-2)
    return fib[n]


print(solution(int(input())))
