# задача не решена

def solution(matrix):
    diags = {i: [] for i in range(-len(matrix), len(matrix[0]))}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            diags[i - j].append(matrix[i][j])

    diags = {k: sorted(v) for k, v in diags.items()}
    print(diags)


print(solution([[4, 5, 6], [1, 2, 3]]))

