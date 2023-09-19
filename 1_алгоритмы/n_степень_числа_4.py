# Необходимо проверить, что введенное число является степенью 4

import math

k = int(input())

if math.log(k, 4).is_integer():
    print('True')
else:
    print('False')
