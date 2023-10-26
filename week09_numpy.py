import numpy as np

np_1d = np.arange(1, 10, 2)
# np_1d = np.arange(1.0, 10.0, 2.0)
print(np_1d)

np_1d = np_1d.reshape(1, 5)  # reshape: 모양 바꾸는 것.
print(np_1d)

def info(x):
    print(f"배열의 차원은 {x.ndim} 입니다.")
    print(f"배열의 shape는 {x.shape} 입니다.")
    print(f"배열의 원소의 개수는 {x.size} 입니다.")
info(np_1d)

print(np_1d, type(np_1d))
print(np_1d, type(np_1d[0]))
print(np_1d.ndim)
print(np_1d.size)
print(np_1d.shape)

# import numpy as np
#
# any_list = [1, "university", 3.91, (5, 7)]
# converted_any_lise = ["1", "university", "3.91", "(5, 7)"]
# # one_type_np = np.array[(2, 4, 6, 8)]
# np_1d = np.array([2, 4, 6, 8])
# np_2d = np.array([[2, 4], [6, 8]])
# print(np_1d.ndim, np_2d.ndim)
# print(np_1d.size, np_2d.size)
# print(np_1d.shape, np_2d.shape)
#
# for i in any_list:
#     print(i)
#     # c++과 달리 데이터 타입이 다 달라도 출력 가능.
