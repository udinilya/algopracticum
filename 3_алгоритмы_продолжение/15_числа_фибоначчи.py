
def solution(n):
    x = 1
    y = 1

    for i in range(2, n+1):
        x, y = y, (x + y) % 10

    print(y)


solution(int(input()))
