# В n строках записаны названия кружков. Необходимо вывести названия уникальных кружков в порядке их ввода

n = int(input())
groups = list(iter(input, '')) # Ввод каждого названия отдельной строкой

unique_groups = []

for group in groups:
    if group not in unique_groups:
        unique_groups.append(group)

for group in unique_groups:
    print(group)
