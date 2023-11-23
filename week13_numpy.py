import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
# print(titanic.describe())#통계 수치
# print(titanic.info())
# print(titanic.head)
# print(titanic.tail())

print(type(titanic))
#결집체 정보 출력
print(titanic.isnull())