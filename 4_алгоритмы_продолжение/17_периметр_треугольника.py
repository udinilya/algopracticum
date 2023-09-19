# Даны длины сторон треугольника. Определить максимально возможный периметр треугольника
# Из отрезков можно составить треугольник если выполняется неравенство c < a + b

nums = list(map(int, input().split()))


def solution(nums):
    nums.sort(reverse=True)
    for el in range(len(nums)-2):
        if nums[el] < nums[el+1] + nums[el+2]:
            return nums[el] + nums[el+1] + nums[el+2]


print(solution(nums))
