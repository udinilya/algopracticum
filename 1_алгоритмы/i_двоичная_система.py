# Необходимо вывести сумму двух двоичных чисел

a = list(map(int, input()))[::-1]
b = list(map(int, input()))[::-1]

res_num = []
prev_overflow = 0

if len(a) > len(b):
    while len(a) != len(b):
        b.append(0)
else:
    while len(a) != len(b):
        a.append(0)

for n in range(len(a)):
    result = a[n] + b[n] + prev_overflow
    prev_overflow = 0
    if result == 0:
        res_num.append(0)
    elif result == 1:
        res_num.append(1)
    elif result == 2:
        res_num.append(0)
        prev_overflow = 1

if prev_overflow == 1:
    res_num.append(prev_overflow)

print(*res_num[::-1], sep='')
