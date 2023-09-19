from itertools import combinations
from functools import reduce

n = int(input())
num = list(combinations(map(int, input().split()), 3))

res = [reduce(lambda a, b: a*b, i) for i in num if sum(i) == 0]

if len(res) > 0 and max(res) >= 0:
    print(max(res))
else:
    print(-1)
