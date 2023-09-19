# Выести матрицу в перевернутом виде(ряд стал столбиком)

matrix = list(iter(input, ''))

rows = [i[::-1] for i in matrix]

pools = [[*tuple(pool)] for pool in rows]

matrix_inv = [[0 for j in range(len(pools))] for i in range(len(pools[0]))]

for i in range(len(pools)):
    for j in range(len(pools[0])):
        matrix_inv[j][i] = pools[i][j]

for i in matrix_inv:
    print(*i)
