# Нужно вывести алфавит до указанной буквы. Здесь без рекурсии

alph = {0: 'a', 1:'b', 2:'c'}


def solution(n):
    buk = []
    i = 0
    while alph[i] < n:
        buk.append(alph[i])
        i += 1
    buk.append(n)
    print(buk)


solution('b')
