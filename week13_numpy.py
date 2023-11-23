import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
#결측값 정보 출력, 15개 필드의 결측값
# print(titanic.isnull().sum())

print(titanic['age'].fillna(titanic['age'].median(), inplace=True))
# age 필드 값 출력, 결측 공간에 중앙값 넣기. inplace 넣어서 변경된 값을 적용

print(titanic.tail())

# titanic['deck'].fillna('Unknown', inplace=True)

titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
titanic['deck'].fillna('Unknown', inplace=True)
print(titanic['deck'].tail(10))
