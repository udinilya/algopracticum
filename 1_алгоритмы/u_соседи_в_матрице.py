# Вывести список соседей по матрице для введенной ячейки в порядке возрастания

n = int(input()) # количество строк
m = int(input()) # количество столбцов
matrix = [input().split() for i in range(n)]
x = int(input()) # координаты ячейки, для которой ищем соседей
y = int(input()) # координаты ячейки, для которой ищем соседей

neighbors = []

if x != 0:
    neighbors.append(matrix[x-1][y])

if x != n-1:
    neighbors.append(matrix[x + 1][y])

if y != 0:
    neighbors.append(matrix[x][y - 1])

if y != m-1:
    neighbors.append(matrix[x][y + 1])

print(*sorted(neighbors))
