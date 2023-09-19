# Нужно посчитать сколько единиц содержится в двоичной форме введенного числа
k = format(int(input()), 'b')

count = 0
for i in k:
    if int(i) == 1:
        count += 1

print(count)
