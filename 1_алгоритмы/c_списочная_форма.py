# В первой строке длина срисочной формы числа, во второй строке само число. Необходимо вернуть
# списочную форму числа x+k


length_x = int(input())
x = map(int, input().split())
k = int(input())

num_x = []

for i in x:
    num_x.append(i)

num_new = (int(''.join(map(str, num_x))))+k

print(' '.join(str(num_new)))
