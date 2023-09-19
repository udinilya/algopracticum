# Две строки s и t считаются равными, если можно заменить символы s и получить t. Например, если строка s=abacaba,
# то ей будет равна строка t=xhxixhx, так как все вхождения «a» заменены на «x», «b» — на «h», а «c» — на «i».
# Все вхождения символа должны быть заменены с сохранением порядка. Два разных символа одной строки не могут
# соответствовать одинаковому символу из другой строки.

s = 'abacaba'
t = 'xhxixhx'


def solution(s, t):
    first = {el: [] for el in s}
    for idx, el in enumerate(s):
        first[el].append(idx)

    second = {el: [] for el in t}
    for idx, el in enumerate(t):
        second[el].append(idx)

    if list(first.values()) == list(second.values()):
        return 'YES'
    else:
        return 'NO'


print(solution(s, t))
