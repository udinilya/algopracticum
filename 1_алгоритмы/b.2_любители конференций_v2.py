# Второй вариант решения
# Дана колонки с id вузов и количеством участников коныеренции от каждого вуза
# Нужно вывести id вузов отсортированных по количеству участников начиная с максимального в порядке убывания участников

ids = map(int, input().split())
k = int(input())

count = dict()
for i in ids:
    try:
        count[i] += 1
    except KeyError:
        count[i] = 1

popularity = sorted(count.items(), key=lambda x: x[1], reverse=True)
most_popular = list(map(lambda x: x[0], popularity))[:k]

print(*most_popular)
