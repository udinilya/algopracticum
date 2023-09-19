def solution(n, m, matrix):
    neighbors = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 1:
                if x == 0:
                    neighbors.append(0)
                if y == 0:
                    neighbors.append(0)
                if x == n-1:
                    neighbors.append(0)
                if y == m-1:
                    neighbors.append(0)

                if x != 0:
                    neighbors.append(matrix[x-1][y])
                if x != n-1:
                    neighbors.append(matrix[x + 1][y])
                if y != 0:
                    neighbors.append(matrix[x][y - 1])
                if y != m-1:
                    neighbors.append(matrix[x][y + 1])

    return neighbors.count(0)


print(solution(4, 4, [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
