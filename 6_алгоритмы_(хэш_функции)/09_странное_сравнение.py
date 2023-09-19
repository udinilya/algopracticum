# Две строки s и t считаются равными, если можно заменить символы s и получить t. Например, если строка s=abacaba,
# то ей будет равна строка t=xhxixhx, так как все вхождения «a» заменены на «x», «b» — на «h», а «c» — на «i».
# Все вхождения символа должны быть заменены с сохранением порядка. Два разных символа одной строки не могут
# соответствовать одинаковому символу из другой строки.

def get_hash(string):
    result = {el: [] for el in string}
    for idx, el in enumerate(string):
        result[el].append(idx)
    return list(result.values())


def solution(first, second):
    return get_hash(first) == get_hash(second)


print(solution('add', 'ghh'))
