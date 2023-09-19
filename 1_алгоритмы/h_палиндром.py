# Проверить, что слово является палиндромом

word = input()

new_word =[]

for i in word:
    if i.isalpha() or i.isalnum():
        new_word.append(i.lower())

if new_word == new_word[::-1]:
    print('True')
else:
    print('False')
