# Дан массив цен на бирже по дням.
# Нужно вывести число, равное максимально возможной прибыли за эти дни.
# Акции можно продавать только по одной штуке. И в один день возможна только одна транзакция.

prices = list(map(int, input().split()))

profit = 0
count = 0

for i in range(len(prices)-1):
    if prices[i] < prices[i+1] and count == 0:
        profit -= prices[i]
        count += 1
    elif prices[i] < prices[i + 1] and count == 1:
        pass
    elif prices[i] > prices[i + 1] and count == 0:
        pass
    elif prices[i] > prices[i + 1] and count == 1:
        profit += prices[i]
        count -= 1

if prices[-1] and count == 0:
    pass
elif prices[-1] and count == 1:
    profit += prices[-1]

print(profit)
