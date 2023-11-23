import numpy as np

a = np.array([1, 3, 5, 7])  # 네 가지 원소를 가진 배열
print(a)
print(a.ndim)  # 차원

b = np.array([[1, 3, 5, 7], [5, 6, 7, 8], [7, 8, 9, 3]])
print(b.shape, b.strides)

c = np.array([[1, 3, 5, 7], [5, 6, 7, "8"], [7, 8, 9, 3]])
print(c, c.dtype)

#ndim, shape, dtype
#배열의 차원 수, 배열의 차원과 크기를 나타내는 튜플 형태의 속성, 배열 요소의 데이터 타입을 나타내는 속성
#strides

d = np.arange(5, 10, 2)
print(d)

a1 = np.ones(5)
a2 = np.array([1, 1, 1, 1, 1])
a3 = np.arange(5)*0+1
a4 = np.zeros(5)+1
a5 = np.linspace(1, 1, 5)
a6 = np.full(5, 1)

