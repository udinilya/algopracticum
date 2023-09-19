# Нужно вывести индекс искомого элемента в массиве
# Использовать сортировку и вспомогательные массивы, сеты и словари нельзя

n = 3
data = [5, 6, 7, 9, 0, 1, 3, 4]

idx = -1


def solution(data, idx):
    if not len(data):
        return -1
    else:
        for el in data:
            if el == n:
                idx += 1
                return idx
            else:
                idx += 1
                del data[0]
                return solution(data, idx)


print(solution(data, idx))
