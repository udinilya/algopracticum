# Нужно вывести n-ное число Фибоначчи
# Реализовано с рекурсией

def solution(n):
    if n == 0 or n == 1:
        return 1
    return solution(n-1) + solution(n-2)


print(solution(int(input())))
