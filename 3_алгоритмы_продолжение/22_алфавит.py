# Нужно вывести алфавит до указанной буквы. Решение с рекурсией

letters = ['a', 'b', 'c']


def solution(n):
    if n == 'a':
        return 'a'
    index = letters.index(n)
    return n + solution(letters[index-1])


print(*reversed(''.join(solution('b'))))
