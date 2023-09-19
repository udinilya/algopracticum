# Дано равное количество чётных и нечётных элементов массива. Нужно вывести четные на чётных индексах
# и нечетные, соответственно, на нечётных. Исходный порядок внутри групп менять нельзя

data = [6, 1, 1, 5, 2, 4, 4, 5]


def solution(data):
    even = [i for i in data if i % 2 == 0]
    odd = [i for i in data if i % 2 == 1]

    new_data = []
    for elem in zip(even, odd):
        for i in elem:
            new_data.append(i)

    return new_data


print(*solution(data))
