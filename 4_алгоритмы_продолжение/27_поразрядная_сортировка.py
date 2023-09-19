# Написать алгоритм поразрядной сортировки radix sort

def solution(nums: list[int]):
    buckets = [[] for _ in range(10)]

    max_num = 0
    for num in nums:
        digit = num % 10
        buckets[digit].append(num)

        if num > max_num:
            max_num = num

    iterations = len(str(max_num)) - 1

    for i in range(2, iterations + 2):
        new_buckets = [[] for _ in range(10)]

        for bucket in buckets:
            for num in bucket:
                radix = num % (10 ** i) // (10 ** (i - 1))
                new_buckets[radix].append(num)

        buckets = new_buckets

    return [i for bucket in buckets for i in bucket]


print(solution([133, 12, 2]))
