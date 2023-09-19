# Проверить, что слова являются анаграммой

a = input()
b = input()

if sorted(a) == sorted(b):
    print("True")
else:
    print("False")
