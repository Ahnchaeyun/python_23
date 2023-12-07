import numpy as np

# numpy 배열
# 1. 동일한 데이터 타입의 원소만 저장
# 2. 메모리에 연속적으로 저장되어 빠른 속도로 데이터 처리 가능
#
# np = np.arange(1, 10, 2)
# np = np.reshape(1, 5)
# 1. info(np): 차원, shape, 원소 개수
# 2. type(np): 타입
# 3. np.ndim: 차원
# 4. np.szie: 개수
# 5. np.shape: 모양
#
# error = [1, "error", 1.5, (1,2)]
# right = ["1", "error", "1.5", "(1,2)"]
# 1. error_np = np.array(error)
# 2. right_np = np.array(right)
# = 문자열 외에 다른 타입의 튜플이 포함된 리스트를 numpy로 변환 시, 오류 발생

np_1d = np.arange(1, 10, 2)
print(np_1d)

np_1d = np_1d.reshape(1, 5)  # reshape: 모양 바꾸는 것.
# 생성한 배열의 모양을 1행 5열로 변경
print(np_1d)

#배열의 차원, shape, 원소의 개수를 출력하는 함수
def info(x):
    print(f"배열의 차원은 {x.ndim} 입니다.")
    print(f"배열의 shape는 {x.shape} 입니다.")
    print(f"배열의 원소의 개수는 {x.size} 입니다.")
info(np_1d)

print(np_1d, type(np_1d))
print(np_1d, type(np_1d[0])) #배열의 첫 번째 원소와 원소의 타입을 출력
print(np_1d.ndim)
print(np_1d.size) #원소의 개수
print(np_1d.shape) #원소의 모양

np_1d = np.array([2, 4, 6, 8])
np_2d = np.array([[2, 4], [6, 8]])
print(np_1d.ndim, np_2d.ndim) #원소의 차원
print(np_1d.size, np_2d.size)
print(np_1d.shape, np_2d.shape)

any_list = [1, "university", 3.91, (5, 7)]
converted_any_list = ["1", "university", "3.91", "(5, 7)"] #원소를 문자열로 변환
one_type_np_list = np.array(converted_any_list) #문자열로 변환된 리스트를 넘파이 배열로 변환
# one_type_np_list = np.array(any_list)  # ValueError
#문자열 외에 다른 타입의 튜플이 포함된 리스트를 넘파이로 변환하면 오류 발생

for i in any_list:
    print(i)

for j in one_type_np_list:
    print(j)


for i in any_list:
    print(i)
    # c++과 달리 데이터 타입이 다 달라도 출력 가능.
