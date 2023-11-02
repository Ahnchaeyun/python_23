import numpy as np
a0 = np.ones((2, 3))
a1 = a0[:, 2]+1
print(a1)
a2 = np.full((3,3), 5)
print(a2)
a3 = np.eye(3) #단위 행렬
print(a3)

a4 = a3[:2, 1:]
print(a4)

a5 = a3[2]
a6 = a3[1, :]
a7 = a3[2:, :]
#결국 다 같은 값

print(a7)