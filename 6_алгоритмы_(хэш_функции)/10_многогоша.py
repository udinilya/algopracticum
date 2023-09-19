# Дана строка, состоящая из букв «G», «O», «S», «H», «A». Нужно найти все подстроки длины 10, которые встречаются
# более одного раза и вывести их в алфавмтном порядке.

def get_substrings(word):
    substrings = [word[el:el+10] for el in range(len(word))]
    substrings_count = {el: substrings.count(el) for el in substrings if len(el) == 10}
    required_substrings = sorted([key for key, value in substrings_count.items() if value > 1])

    return required_substrings


print(*get_substrings('gggggooooogggggoooooogggggssshaa'))
print(*get_substrings('ggggggggggg'))
