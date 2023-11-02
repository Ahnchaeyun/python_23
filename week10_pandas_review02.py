import numpy as np
a0 = np.ones((2, 3))
a1 = a0[:, 2]+1
print(a1)
print(a0)
# a1 = np.array([
#     [1, 1, 2],
#     [1, 1, 2],
#     [1, 1, 2]
# ])
a2 = np.array([
    [1, 0, 0],
    [2, 0, 0],
    [1, 0, 0]
])
print(a2)
# print(np.dot(a1, a2))
# print(np.matmul(a1, a2))