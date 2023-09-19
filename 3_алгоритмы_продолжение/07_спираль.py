# Выести на печать элементы матрицы по спирали

n = int(input())
matrix = [input().split() for i in range(n)]

spiral = []

while matrix:
    if matrix:
        for i in matrix[0]:
            spiral.append(i)

        matrix.remove(matrix[0])

    if matrix:
        for i in matrix:
            if len(i) > 1:
                spiral.append(i[-1])
                i.remove(i[-1])
            elif len(i) == 1:
                for el in matrix:
                    spiral.append(el[0])
                matrix.clear()

    if matrix:
        for i in matrix[-1][::-1]:
            spiral.append(i)

        matrix.remove(matrix[-1])

    if matrix:
        for i in matrix[::-1]:
            spiral.append(i[0])
            i.remove(i[0])

print(spiral)
