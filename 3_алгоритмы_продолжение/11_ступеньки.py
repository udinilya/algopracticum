# Можно ли добраться до верхней ступеньки лестницы?
# Для каждой ступеньки известно, на какое мксимальное количество ступенек можно с нее допрыгнуть

steps = list(map(int, input().split()))

i = 0
while i <= len(steps)-1:
    if steps[i] == i:
        print(False)
        break
    i += steps[i]
else:
    print(True)
