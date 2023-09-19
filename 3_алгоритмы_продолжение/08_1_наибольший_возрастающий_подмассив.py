row = list(map(int, input().split()))

count = 1
max_rise = 0

for i in range(len(row)-1):
    if row[i] < row[i+1]:
        count += 1
    else:
        if count == 1:
            count = 0
        else:
            count = 1
max_rise = max(max_rise, count)

print(max_rise)
