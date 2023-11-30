"""
1) 생존자와 사망자 수를 구하시오.
2) 남성과 여성의 생존률을 구하시오.
3) 객실 등급별 생존자 수를 구하시오.
4) 나이대별 생존자 수를 구하시오.
5) 나이분포 시각화
"""
import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

survived_ages = titanic[titanic['survived']==1]['age'].dropna()
dead_ages = titanic[titanic['survived']==0]['age'].dropna()

plt.hist(survived_ages, bins=20, label='survived', alpha=0.5)
plt.hist(dead_ages, bins=20, label='dead', alpha=0.5)
plt.xlabel('age')
plt.ylabel('count')
plt.legend()
plt.show()
