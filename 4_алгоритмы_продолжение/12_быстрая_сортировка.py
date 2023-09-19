# реализовать алгоритм быстрой сортировки

array = [4, 3, 2, 1]


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort(array))
