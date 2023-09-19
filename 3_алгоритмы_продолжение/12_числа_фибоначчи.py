# Нужно вывести n-ное число Фибоначчи

def solution(n):
    x = 1
    y = 1
    row = {0: 1, 1: 1}

    for i in range(2, n+1):
        row[i] = x + y
        x = y
        y = row[i]

    print(row[n])


solution(int(input()))
