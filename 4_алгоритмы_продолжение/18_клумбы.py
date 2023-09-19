# Нужно вывести число получившихся клумб.
# Даны n садовников и координаты участков земли


def solution(coords):
    coords.sort()
    result = [coords[0]]

    for item in coords[1:]:
        last = result[-1]

        if int(item[0]) > int(last[1]):
            result.append(item)

        else:
            result[-1] = (last[0], max(int(item[1]), int(last[1])))

    return result


n = int(input())
coords = [input().split() for i in range(n)]

print(solution(coords))
