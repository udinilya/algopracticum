# Вычислить сумму чисел от 0 до n с использованием рекурсии

def findsum(n):
    if n == 0:
        return n
    else:
        return n + findsum(n - 1)


print(findsum(5))
