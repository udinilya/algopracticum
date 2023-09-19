# Нужно вывести n-ное число Фибоначчи
# Решение за О(n) по времени и без использования доп. памяти

def solution(n):
    x = 1
    y = 1

    for i in range(2, n+1):
        x, y = y, x+y

    print(y)


solution(int(input()))
