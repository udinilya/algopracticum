# Гоша и Тимофей играли в компьютерную игру Барсучок, и записывали свои очки в каждом раунде. Нужно выяснить,
# какое максимальное количество раундов подряд ребята зарабатывали одинаковые очки.

def get_substrings(string):
    substring = []
    for idx, el in enumerate(string):
        for i in range(1, len(string[idx:])+1):
            substring.append(string[idx:][0:i])

    return substring


def solution(s, t):
    intersecting_substrings = sorted(
        [i for i in get_substrings(s) for j in get_substrings(t) if i == j or i[::-1] == j],
        key=len
    )

    return len(intersecting_substrings[-1])


print(solution([1, 2, 3, 4, 5], [4, 5, 9]))
