# Двны строки одинаковой длины. Нужно выести количество столбцов, которые осторитрованы не по неубыванию

letters = list(iter(input, ''))

rows = [i[::] for i in letters]

pools = [[*tuple(pool)] for pool in rows]

letters_inv = [[0 for j in range(len(pools))] for i in range(len(pools[0]))]

for i in range(len(pools)):
    for j in range(len(pools[0])):
        letters_inv[j][i] = pools[i][j]


count = 0
for i in letters_inv:
    if i != sorted(i):
        count += 1

print(count)
