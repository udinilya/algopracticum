# Вывести значение корня из двух с точностью пять знаков
# Серёжино решение

def sqrt2(x):
    precission = 10 ** -5
    x_next = (2 + x ** 2) / (2 * x)
    
    if (x_next - precission) ** 2 < 2:
        return x_next
    return sqrt2(x_next)


s = str(sqrt2(1.0))
