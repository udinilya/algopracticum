# Необходимо вывести повторы первого списка во втором, в порядке, как они даны в первом списке
# Используется бинарный поиск

values = [4, 9, 5, 9, 2]
a = [4, 9, 8, 4, 9, 8, 4, 2, 2]

search = []

for i in values:
    a.sort()
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != i and low <= high:
        if i > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low <= high:
        search.append(a[mid])

print(search)
