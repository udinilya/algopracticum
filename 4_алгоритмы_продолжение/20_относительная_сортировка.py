# Необходимо сделать сортировку массива так, что бы в начале цифры располагалась как в образце
# а потом шли оставшиеся цифры в порядке обычной сортировки

nums = [2, 4, 3, 4, 8, 6]
sample = [2, 4, 3]


def solution(sample, nums):
    count = dict.fromkeys(sample, 0)
    not_in_sample = []

    for el in nums:
        if el in sample:
            count[el] += 1
        else:
            not_in_sample.append(el)

    not_in_sample.sort()

    new_nums = [[item] * count[item] for item in sample]

    sort_nums = []
    for el in new_nums:
        for i in el:
            sort_nums.append(i)

    return *sort_nums, *not_in_sample


print(*solution(sample, nums))
