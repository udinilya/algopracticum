# Кондратий захотел выяснить k - ю минимальную разницу между значениями треш-индексов городов Трешландии.
# Под разницей элементов a и b понимаем |a - b|. Выведите k - ую минимальную разницу между парами
# значений треш - индексов.

values = [1, 3, 5]
k = 3


def solution(values):
    douplicate_values = values
    diffs = []
    for idx, i in enumerate(values):
        for id, j in enumerate(douplicate_values):
            if idx != id and idx < id:
                diffs.append(abs(i-j))

    diffs.sort()
    return diffs[k-1]


print(solution(values))
