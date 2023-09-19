# Дано количество призеров. Нужно вывести True, если можно разделить имеющиеся монеты поровну на всех

n_people = 4
coins = [4, 3, 2, 3, 5, 2, 1]


def remove_at_indices(values, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        values.pop(idx)
    return values


def solution(left_coins):
    if not len(left_coins):
        return True

    cur_sum = 0
    used_coins = []
    for i, coin in enumerate(left_coins):
        used_coins.append(i)
        if cur_sum + coin == coins_for_person:
            remove_at_indices(left_coins, used_coins)
            return solution(left_coins)
        elif cur_sum + coin < coins_for_person:
            cur_sum += coin
        else:
            used_coins.pop()

    return False


coins_for_person = int(sum(coins) / n_people)
if sum(coins) % n_people != 0:
    print(False)
else:
    print(solution(coins))
