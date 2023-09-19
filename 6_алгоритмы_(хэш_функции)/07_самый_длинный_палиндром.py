# Выведите единственное число — длину наибольшего палиндрома, который можно составить из букв строки.

def solution(word):
    count = 0

    alphas = {el: word.count(el) for el in word}

    for key, value in alphas.items():
        if value % 2 == 0:
            count += value
        else:
            count += value - 1

    if any(res % 2 == 1 for res in alphas.values()):
        count += 1

    return count


print(solution('abccccdd'))
