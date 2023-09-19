# Дана строка, состоящая из букв «G», «O», «S», «H», «A». Нужно найти все подстроки длины 10, которые встречаются
# более одного раза и вывести их в алфавмтном порядке.

def solution(string):
    counts = dict()
    for i in range(0, len(string)-9):
        slice_ = string[i:i+10]
        try:
            counts[slice_] += 1
        except KeyError:
            counts[slice_] = 1

    return sorted(slice_ for slice_, count in counts.items() if count > 1)


print(solution('gggggooooogggggoooooogggggssshaa'))
