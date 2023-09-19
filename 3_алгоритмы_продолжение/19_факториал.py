# Вывести факториал числа с помощью цикла

def factorial(n):
    fac = 1
    for i in range(2, n+1):
        fac *= i
    return fac


print(factorial(5))
