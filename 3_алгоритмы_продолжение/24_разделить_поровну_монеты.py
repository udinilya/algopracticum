# Дано количество призеров. Нужно вывести True, если можно разделить имеющиеся монеты поровну на всех
# Задача не решена до конца

n = int(input())
coins = list(map(int, input().split()))

sum_of_coins = 0

for i in coins:
    sum_of_coins += i

prize = sum_of_coins // n

if sum_of_coins % n != 0:
    print('False')


current_sum = []

def solution(coins):
    if len(coins) == 0:
        pass
    elif len(coins) == 1:
        if coins[-1] == prize:
            current_sum.append(coins[-1])
    else:
        if coins[0] == prize:
            current_sum.append(coins[0])
            solution(coins[1:])
        else:
            cur = coins[0] + coins[1]
            if cur == prize:
                current_sum.append(cur)
                solution(coins[2:])

    return current_sum


print(solution(coins))
