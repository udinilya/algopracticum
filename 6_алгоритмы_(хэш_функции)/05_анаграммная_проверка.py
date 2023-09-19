# Нужно вывести в отсортированном порядке индексы строк, которые являются анаграммами. В каждой строке должны быть
# индексы строк-анаграмм. Обратите внимание, что группа анаграмм может состоять и из одной строки.
# Например, если в исходном наборе нет анаграмм, то надо вывести n групп, каждая из которых состоит из одного индекса.

def get_hash(string):
    res = 0
    for letter in string:
        order = ord(letter) - 96
        res += 10 ** order

    return res


def solution(arr):
    hashes = {get_hash(string): [] for string in arr}
    for idx, string in enumerate(arr):
        hashes[get_hash(string)].append(idx)

    return list(hashes.values())


print(solution(['tan', 'eat', 'tea', 'ate', 'nat', 'bat']))
