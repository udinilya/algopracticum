# Вывести все возможные скобочные последовательности в лексографическом порядке

def solution(n):
    if n == 1:
        return ['()']
    else:
        x = list(solution(n-1))
        y = [elem + '()' for elem in x]
        z = ['()' + elem for elem in x]
        t = ['(' + elem + ')' for elem in x]
        res = list(set(y + z + t))
    return res


print('\n'.join(sorted(solution(3))), end='')
