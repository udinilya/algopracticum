# Вывести длину последнего слова строки

row = input()

last_whitespace = row.rfind(' ')

print(len(row[last_whitespace+1:]))
