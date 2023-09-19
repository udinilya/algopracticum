# Дан массив, где одно число встречается более одного раза
# Выведите это число

k = int(input())
n = list(map(int, input().split()))

for i, x in enumerate(n):
    if x in n[:i]:
        print(x)
        break
