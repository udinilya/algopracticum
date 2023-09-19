# На клавиатуре телефона цифре соответвует несколько букв.
# Дана комбинация из цифр 2-9. Выести все сочетания букв через пробел для этой комбинации.

from itertools import product

num = map(int, input())

comb = {2: 'abc',
        3: 'def',
        4: 'ghi'}

all_var = [comb[i] for i in num]

for t in list(product(*all_var)):
    print(''.join(t), end=' ')
