"""
1) 생존자와 사망자 수를 구하시오.
2) 남성과 여성의 생존률을 구하시오.
3) 객실 등급별 생존률을 구하시오
4) 나이별 생존자 수
"""
import seaborn as sns
import pandas as pd
titanic = sns.load_dataset('titanic')

# pclass_survived = titanic.groupby('pclass')['survived'].sum()
# print(pclass_survived)
# age_survived = titanic.groupby('age')['survived'].sum()

age_survived = titanic.groupby(pd.cut(titanic['age'], bins=[0,10,20,30,40,50,60,70,80]))['survived'].sum()

print(age_survived)
