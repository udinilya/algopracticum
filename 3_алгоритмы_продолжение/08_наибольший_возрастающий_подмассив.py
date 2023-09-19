# Вывести длину наибольшего возрастающего подмассива

row = list(map(int, input().split()))

count = 0
rising = 0

for i in range(len(row)-1):
    if row[i] < row[i+1]:
        count += 1
    else:
        if count == 0:
            pass
        else:
            count += 1
            if count > rising:
                rising = count
            count = 0

if row[-1] and row[-1] > row[-2]:
    count += 1
    if count > rising:
        rising = count

print(rising)
