# Вывести самое большое число, которое можно составить из предложенных чисел

numbers = [2, 100, 32]


def solution(numbers):
    num = []
    for i in numbers:
        num.append(str(i))

    for j in range(len(num)-1):
        for k in range(j, len(num)):
            if num[j][0] < num[k][0]:
                num[j], num[k] = num[k], num[j]

    return ''.join(num)


print(solution(numbers))
