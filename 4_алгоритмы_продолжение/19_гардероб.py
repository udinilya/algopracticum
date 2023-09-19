# Нужно расположить номера одежды из массива в порядке возрастания
# Нужно все сделать за один проход по массиву, то есть использовать различные сортировки нельзя

pool = [0, 2, 1, 2, 0, 2, 1]


def solution(pool):
    one = []
    two = []
    three = []
    for item in pool:
        if item == 0:
            one.append(item)
        elif item == 1:
            two.append(item)
        else:
            three.append(item)

    return *one, *two, *three


print(*solution(pool))
