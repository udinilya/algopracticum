# Вывести значение НОД для двух чисел

a = int(input())
b = int(input())


def solution(a, b):
    a, b = max(a, b), min(a, b)
    res = a % b

    if res == 0:
        return b
    return solution(b, res)


print(solution(a, b))
