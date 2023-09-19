# На клавиатуре телефона цифре соответвует несколько букв.
# Дана комбинация из цифр 2-9. Выести все сочетания букв через пробел для этой комбинации.

num = list(map(int, input()))

comb = {2: 'abc',
        3: 'def',
        4: 'ghi'}

all_var = [comb[i] for i in num]

pools = [tuple(pool) for pool in all_var]

result = [[]]
for pool in pools:
    result = [x+[y] for x in result for y in pool]

for prod in result:
    print(''.join(prod), end=' ')
