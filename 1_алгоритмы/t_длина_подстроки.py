# Введена строка латинских символов
# Необходимо вывести длину максимальной подстроки

row = input()

# ищем второе вхождение символа
alpha = ''

for i in row:
    s = row.find(i, row.find(i)+1)
    if s != -1:
        alpha = s

# делим строку на подстроки по этому символу
division = row.split(row[alpha])

lenght = []
for i in division:
    lenght.append(len(i)+1)

print(max(lenght))
