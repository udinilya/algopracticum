# Нужно вывести алфавит до указанной буквы. Решение с рекурсией

alph = ['a', 'b', 'c', 'd']
s = []


def solution(n):
    if alph.index(n) == 0:
        s.append(alph[0])
    else:
        s.append(n)
        solution(alph[alph.index(n)-1])
    return s


print(*reversed(solution('c')))
