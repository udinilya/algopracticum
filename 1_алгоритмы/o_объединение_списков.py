# Необходимо объединить списки a, b и выести отсортированный результат.
# Встроенные функции использовать нельзя

a = list(map(int, input().split()))
m = int(input()) # количество нулей в конце первой строки
k = int(input())
b = list(map(int, input().split()))

a = a[:-m]

for i in b:
    a.append(i)

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
