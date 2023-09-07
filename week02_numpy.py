import numpy as np
import random

v = np.array([
    [1, 3, -9, 2],
    [71, 13, -22, 7]
])

print(v.ndim, v.shape, v.data, v.dtype, v.strides)

number = list(map(int, input().split()))
print(number)

n = int(input("input number : "))
l = list()
for i in range(n):
    l.append(random.randint(1, 100))



