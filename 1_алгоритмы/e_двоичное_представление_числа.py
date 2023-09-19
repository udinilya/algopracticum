# Нужно вывести двоичное представление числа

k = int(input())

bin = []

num = k // 2
ostat = k % 2
bin.append(ostat)

while num >= 2:
    new_num = num // 2
    new_ostat = num % 2
    bin.append(new_ostat)
    num = new_num
    if num == 1:
        bin.append(num)


print(*bin[::-1], sep='')
