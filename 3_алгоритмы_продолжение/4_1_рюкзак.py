# Реализовать алгоритм - взять наиболее ценный предмет, из тех, которые уместятся в рюкзак
# Выбрать следующий по стоимости предмет, при условии, что в рюкзаке осталось место
# Если стоимость предметов одинаковая, то выбрать предмет с наименьшим весом
# Вывести индексы отобранных предметов

# Простой способ решения с использованием двойной сортировки

size = int(input())
n = int(input())
items = [list(map(int, input().split())) for _ in range(n)]

result_items = []
current_size = 0

items.sort(key=lambda i: (-i[0], i[1]))

for item in items:
    if current_size + item[1] <= size:
        result_items.append(item)
        current_size += item[1]

print(items)
print(result_items)
