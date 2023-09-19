# Дана строка, необходимо ее осортировать по частоте вхождения букв начиная с самой большой.
# Если частота букв одинаковая, необходимо сделать дополнительную сортировку - лексикографическую

s = list(input())

dic = {}

for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

inv_map = {}
for k,v in dic.items():
    inv_map[v] = inv_map.get(v,[]) + [k]

new_string = ""
for key in sorted(inv_map):
    for el in sorted(inv_map[key], reverse=True):
        new_string += el*key

print(new_string[::-1])
