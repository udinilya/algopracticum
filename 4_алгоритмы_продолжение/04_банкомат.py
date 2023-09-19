# Нужно вывести число способов, которым можно набрать указанную сумму монет

n = 5
coins = sorted([3, 2, 1], reverse=True)

count = 0


def solution(coins, count):
    if not len(coins):
        return count
    else:
        cur_sum = coins[0]
        for coin in coins:
            new_cur_sum = cur_sum + coin

            if new_cur_sum == n:
                count += 1

            elif new_cur_sum < n:
                newly = new_cur_sum
                while newly < n:
                    newly += coins[-1]
                    if newly == n:
                        count += 1

        coins.remove(coins[0])
        return solution(coins, count)


print(solution(coins, count))
