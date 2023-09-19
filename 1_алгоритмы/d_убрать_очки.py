# Вводится число и строка чисел в количестве n
# Необходимо вывести строку исключив все нули

n = int(input())
x = list(map(int, input().split()))

for i in x:
    if i != 0:
        print(i, end=' ')
