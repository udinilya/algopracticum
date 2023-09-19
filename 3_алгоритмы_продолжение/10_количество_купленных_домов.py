# Вывести максимальное число домов, которые можно купить исходя из бюджета

budget = int(input())
cost_of_houses = sorted(list(map(int, input().split())))

amount_of_costs = 0
count = 0

for i in cost_of_houses:
    amount_of_costs += i
    if amount_of_costs <= budget:
        count += 1
    else:
        break

print(count)
