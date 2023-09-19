# Вывести факториал числа с использованием цикла

def factorial(n):
    i = 0
    fac = 1
    while i != n:
        fac *= i+1
        i += 1
    return fac


print(factorial(5))
