# Можно найти такие целые числа, которые при умножение на a и b в сумме дкдут НОД (коэффециенты Безу)
# Выведите в строку два коэффициента и НОД

a = int(input())
b = int(input())
s1 = 1
s2 = 0
t1 = 0
t2 = 1


def nod(a, b, s1, s2, t1, t2):
    quotient = a // b
    remainder = a % b

    new_s = s1 - quotient * s2
    s1 = s2
    s2 = new_s

    new_t = t1 - quotient * t2
    t1 = t2
    t2 = new_t

    if remainder == 0:
        return s1, t1, b
    return nod(b, remainder, s1, s2, t1, t2)


print(nod(a, b, s1, s2, t1, t2))
