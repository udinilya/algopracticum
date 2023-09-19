# Необходимо вывести повторы первого списка во втором
# Решение выведет значения в отсортированном порядке

def solution(first, second):
    first.sort()
    second.sort()

    i, j, res = 0, 0, []
    while i < len(first) and j < len(second):
        if first[i] == second[j]:
            res.append(first[i])
            i += 1
            j += 1
        elif first[i] < second[j]:
            i += 1
        else:
            j += 1
    return res


print(solution([7, 8, 5, 10], [9, 7, 5, 3]))
