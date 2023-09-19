data = [4, 3, 2, 1]


def solution(data):
    for i in range(1, len(data)):
        cur = data[i]
        j = i-1
        while data[j] > cur and j >= 0:
            data[j+1] = data[j]
            j -= 1
            data[j+1] = cur
    return data


print(solution(data))
