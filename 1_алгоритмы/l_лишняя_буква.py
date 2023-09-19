# Введено 2 строки. Вторая строка образована перемешиванием букв первой с добавлением одной лишней буквы
# вывести лишнюю букву

s = list(input())
t = list(input())

united = s + t
alpha = []

for i in united:
    if united.count(i) % 2 != 0 and i not in alpha:
        alpha.append(i)

print(*alpha)
