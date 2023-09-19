# Реализовать алгоритм - взять наиболее ценный предмет, из тех, которые уместятся в рюкзак
# Выбрать следующий по стоимости предмет, при усорвии, что в рюкзаке осталось место
# Если стоимость предметов одинаковая, то выбрать предмет с наименьшим весом
# Вывести индексы отобранных предметов

capacity = int(input())
n = int(input())
items = [input().split() for i in range(n)]

suitable_items = []
suitable_items.extend(items)
valuable_items = []
indexes_valuable_items = []

z = 0
while z < len(items):

# Удаляем все не подходящие по размеру предметы
    y = 0
    while y < len(suitable_items):
        if int(suitable_items[y][-1]) > capacity:
            del suitable_items[y]
        else:
            y += 1

# Определяем самую высокую цену оставшихся предметов
    prices = [0]
    for item in suitable_items:
        prices.append(item[0])

    max_price = max(prices, key=lambda i: int(i))

# Кладем в рюкзак предмет с самой высокой ценой,
# а если таких несколько, то выбираем предмет с наименьшим весом

    double_price_items = [int(item[-1]) for item in suitable_items if item[0] == max_price]
    double_price_items.append(1000)

    min_weight = min(double_price_items, key=lambda i: int(i))

    for x, item in enumerate(suitable_items):
        if item[-1] == min_weight and item[0] == max_price:
            valuable_items.append(item)
            capacity -= int(item[-1])
            del suitable_items[x]
            double_price_items.clear()

    z += 1

# Выводим порядковый номер положенных в рюкзак предметов
d = dict()
for x, item in enumerate(items):
    d[tuple(item)] = x

for item in valuable_items:
    indexes_valuable_items.append(d[tuple(item)])

print(*indexes_valuable_items)
