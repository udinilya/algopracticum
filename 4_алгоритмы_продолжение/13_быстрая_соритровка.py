# оптимизировать алгоритм быстрой сортировки, что бы не задействовать доп. память

def quicksort(arr, left, right):
    if left >= right:
        return x
    mid = (left + right) // 2
    sep = arr[mid]
    i = left
    j = right
    while True:
        while arr[i] < sep:
            i += 1
        while arr[j] > sep:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        if i > j:
            break
    quicksort(arr, left, j)
    quicksort(arr, i, right)
    return x


x = [3, 2, 4, 1]
print(quicksort(x, 0, len(x) - 1))
