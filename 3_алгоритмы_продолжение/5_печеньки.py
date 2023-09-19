# Дан фактор жадности - минимальный размер печеньки, которое возьмет ребенок
# Нужно выяснит, сколько детей останутся довольны. Можно брать только 1 печенье

# Для решения нужно взять самое большое печенье и найти кому его скормить

factor = sorted(list(map(int, input().split())), reverse=True)
size = sorted(list(map(int, input().split())), reverse=True)

count = 0

for i in range(len(size)):
    for j in range(len(factor)):
        if size[i] >= factor[j]:
            count += 1
            factor.remove(factor[j])
            break

print(count)
