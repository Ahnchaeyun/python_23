import pandas as pd
import numpy as np

# pandas
# 데이터 프레임을 생성(행과 열로 구성)
# 행: 관칙치
# 열: 변수
# 1. head(), tail(): 데이터 프레임의 처음 몇 행 또는 마지막 몇 행 반환
# 2. shape(): 행과 열의 개수 반환
# 3. info(): 데이터 프레임 정보
# 4. describe():  데이터 프레임 통계 정보

df = pd.DataFrame({
    'a': [1, 2, np.nan, 4],
    'b':[5, np.nan, 7, 8],
    'c':[9, 10, 11, np.nan]
})
print("1")
print(df)

#df 객체의 결측값을 평균값으로 채운다
#df.fillna(value = ) 에서 value 값으로 None, 1, 0의 결측값을 지정 가능
#1.df.mean() 함수로 데이터프레임 객체의 각 열의 평균값 계산
#2.df,fillna() 메서드로 열의 결측값을 평균값으로 채우기
#3.inplace=True 옵션을 지정해 DataFrame 객체 자체를 수정
df.fillna(df.mean(), inplace=True)
print("2")
print(df)

# for col in df.columns:
#     # print(col)
#     df[col] = np.where(pd.isnull(df[col]), np.mean(df[col]), df[col])
#     #np.where(조건, 참일 때 값, 거짓일 때 값)
#     #1. where 함수로 각 열의 원소가 결측값이면 평균 값, 아니면 원래 값
#     #2. pd.isnull()함수는 원소가 결측값인지 여부 확인
# print("3")
# print(df)

from sklearn.impute import SimpleImputer #결집값 처리 전용 클래스
i = SimpleImputer(strategy='mean')  
#SimpleImputer 객체 생성
#mean 옵션 지정시, 평균값으로 결측값을 처리
df = pd.DataFrame(i.fit_transform(df), columns=df.columns)
#df의 결측값을 SimpleImputer 객체를 사용해서 처리하고 새로운 데이터 프레임 객체 생성
print(df)