# Вывести максимальное количество блоков на которое можно разделить множество для последующнй
# сортировки каждого из блоков отдельно. В примере - первый блок (1,0), второй - (2) и тд.

def criterion(a, b):
    return not b or max(a) < min(b)


def solution(array):
    n_blocks, start, stop = 0, 0, 0

    while stop < len(array):
        stop += 1
        print(array[start:stop], array[stop:])
        if criterion(array[start:stop], array[stop:]):
            n_blocks += 1
            start = stop

    return n_blocks


print(solution([1, 0, 2, 3, 4]))
