import pandas as pd
import numpy as np

df = pd.DataFrame({
    'a': [1, 2, np.nan, 4],
    'b':[5, np.nan, 7, 8],
    'c':[9, 10, 11, np.nan]
})

df.fillna(df.mean(), inplace=True)
print(df)

for col in df.columns:
    # print(col)
    df[col] = np.where(pd.isnull(df[col]), np.mean(df[col]), df[col])
    # 원본 데이터의 (데이터 프레임에) 평균값을 내고, 결집값? 들을 평균으로 채운다.

from sklearn.impute import SimpleImputer #결집값 처리 전용 클래스
i = SimpleImputer(strategy='mean')  #impute 객체
df = pd.DataFrame(i.fit_transform(df), columns=df.columns)
print(df)