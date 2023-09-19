# Определить является ли строка s подпоследовательностью строки t

s = list(input())
t = list(input())

word = []
for el in t:
    if el in s:
        word.append(el)

if word == s:
    print('true')
else:
    print('false')
