# Вывести самую длинную подпоследовательность зашифрованного слова
# Если таких несколько - вывести лексикографически минимальную из них

encrypt = input()
words = list(map(str, input().split()))


def sequence(encrypt, word):
    count = 0
    for alph in encrypt:
        if alph == word[count]:
            count += 1
            if count == len(word):
                return True


def solution(encrypt, words):
    seq_list = [word for word in words if sequence(encrypt, word)]

    length = {item: len(item) for item in seq_list}

    res = [k for k, v in length.items() if v == max(length.values())]

    return min(res)


print(solution(encrypt, words))
