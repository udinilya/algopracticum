# Написать алгоритм поразрядной сортировки radix sort

def solution(numbers):
    nums = list(map(lambda x: str(x), numbers))
    n = (len(str(max(numbers))))

    # добавдяем в начало каждого элемента нужное количество нулей, что бы разрядность всех
    # элементов была равна n (по максимальному элементу)
    my_nums = []
    for i in nums:
        m = n - len(i)
        if len(i) < n:
            my_nums.append(('0'*m) + i)
        else:
            my_nums.append(i)

    # Делаем сортировки по количеству разрядов начиная с последнего разряда
    idx = n-1
    while idx >= 0:
        my_nums.sort(key=lambda x: x[idx])
        idx -= 1

    # Здесь удаляем лишние нули в начале элементов в уже отсортированном списке
    b = []
    for el in my_nums:
        if el[0] == '0' and el[0] != el[-1]:
            b.append(el.replace('0', ''))
        elif el[0] == '0' and el[0] == el[-1]:
            b.append('0')
        else:
            b.append(el)
    my_nums = b

    return my_nums


print(solution([45, 892, 0, 7665, 23, 14, 4]))
