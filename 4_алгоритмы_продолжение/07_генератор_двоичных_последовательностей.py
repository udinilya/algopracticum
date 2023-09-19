# вывести все двоичные последовательности для числа n

def gen(n, pref):
    if n == 0:
        print(pref)
    else:
        gen(n-1, pref + '0')
        gen(n - 1, pref + '1')


print(gen(2, ''))
