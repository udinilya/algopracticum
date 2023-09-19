# Выведите единственное число — хеш заданной строки. a и m заданы.

a = 123
m = 100003


def ascii_codes(word):
    s = []
    for elem in word:
        s.append(ord(elem))

    return s


def solution(word):
    a_in_degree = []
    count = 1
    while count <= len(ascii_codes(word)):
        a_in_degree.append(a**(len(ascii_codes(word))-count))
        count += 1

    return sum((list(map(lambda x, y: x * y, ascii_codes(word), a_in_degree)))) % m


print(solution('HaSH'))
