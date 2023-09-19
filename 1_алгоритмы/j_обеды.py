# Даны id сотрудников, нужно определить единственного, кто внес себя в список отличное от двух количество раз

n = int(input())
ids = list(map(int, input().split()))

for i in ids:
    if ids.count(i) == 1 or ids.count(i) >= 3:
        print(i)
        break
