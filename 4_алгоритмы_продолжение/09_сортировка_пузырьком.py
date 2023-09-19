# Вывести массив в остортированном порядке по возрастанию
# Выполнено с использованием рекурсии, т.е. неэффективно за О(n**2)

data = [3, 2, -4, -8, 5, 0, 6, 5, 12, 1]


def solution(data):
    point = 0
    for el in range(len(data)-1):
        if data[el] > data[el+1]:
           point += 1
    if point == 0:
        return data
    else:
        for el in range(len(data)-1):
            if data[el] > data[el+1]:
                data[el], data[el+1] = data[el+1], data[el]
        return solution(data)


print(*solution(data))
