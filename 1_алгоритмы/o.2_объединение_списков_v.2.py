# Необходимо объединить списки a, b и выести отсортированный результат.
# Встроенные функции использовать нельзя

a = list(map(int, input().split()))
_ = int(input())
_ = int(input())
b = list(map(int, input().split()))

cur = 0
for el in b:
    while el >= a[cur] > 0:
        cur += 1
    a = a[:cur] + [el] + a[cur: -1]

print(a)
