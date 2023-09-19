# Вывести самое большое число, которое можно составить из предложенных чисел

def solution(nums):
    nums = list(map(lambda x: str(x), nums))
    nums.sort(key=lambda x: x[0], reverse=True)

    return ''.join(nums)


print(solution([2, 100, 32]))
