# Проверить, что слова являются анаграммой

a = input()
b = input()

new_word = []
new_word2 = []

if len(a) == len(b):
    for i in a:
        if i not in b:
            print('False')
            break
        else:
            new_word.append(i)
    if len(a) == len(new_word):
        for j in b:
            if j not in a:
                print('False')
                break
            else:
                new_word2.append(j)
else:
    print('False')

if len(new_word) == len(a) == len(new_word2):
    print('True')
