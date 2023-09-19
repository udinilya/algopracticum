# Определить какой символ будет находиться в n строке на k позиции в последовательности бинарных чисел

n = int(input())
k = int(input())


def solution(n):
    if n == 1:
        return ['0']
    else:
        res = list(solution(n - 1))
        row = ''
        for j in res[-1]:
            if j == '0':
                row += '01'
            elif j == '1':
                row += '10'
        res.append(row)

    return res


print(solution(n), solution(n)[-1][k-1])
