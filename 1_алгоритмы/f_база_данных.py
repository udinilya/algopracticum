# Дан массив, где одно число встречается более одного раза
# Выведите это число

k = int(input())
n = map(int, input().split())

num = []
double = []

for i in n:
    if i not in num:
        num.append(i)
    else:
        if i not in double:
            double.append(i)

print(*double)
