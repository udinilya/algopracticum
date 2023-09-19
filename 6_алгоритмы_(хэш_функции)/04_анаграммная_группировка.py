# Нужно вывести в отсортированном порядке индексы строк, которые являются анаграммами. В каждой строке должны быть
# индексы строк-анаграмм. Обратите внимание, что группа анаграмм может состоять и из одной строки.
# Например, если в исходном наборе нет анаграмм, то надо вывести n групп, каждая из которых состоит из одного индекса.

words = ['tan', 'eat', 'tea', 'ate', 'nat', 'bat']


def solution(words):
    idxs = []
    involved = []

    for el in range(len(words)):
        if el not in involved:
            idxs.append([el])

        for elem in range(el+1, len(words)):
            if sorted(words[el]) == sorted(words[elem]) and elem not in idxs[-1]:
                idxs[-1].append(elem)
                involved.append(elem)

    return (item for item in idxs)


for elem in solution(words):
    print(*elem)
