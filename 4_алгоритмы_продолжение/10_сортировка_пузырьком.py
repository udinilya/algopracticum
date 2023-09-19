# Вывести массив в остортированном порядке по возрастанию
# эффективное решение - квадратичная сортировка

data = [3, 2, -4, -8, 5, 0, 6, 12, 1]


def solution(data):
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    return data


print(solution(data))
