# Дана колонки с id вузов и количеством участников коныеренции от каждого вуза
# Нужно вывести id вузов отсортированных по количеству участников начиная с максимального в порядке убывания участников

def top_id():
    id = list(map(int, input().split()))
    k = int(input())

    list_id = {}
    for n in id:
        if n not in list_id:
            list_id[n] = 1
        else:
            list_id[n] += 1

    sorted_id = sorted(list_id.items(), key=lambda x: x[1], reverse=True)[:k] # здесь получаем отсоритрованный кортеж
    print(*list(dict(sorted_id))) # возвращаем вновь словарь и печатаем ключи


top_id()
