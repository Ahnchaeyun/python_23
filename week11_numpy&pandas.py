import pandas as pd
df = pd.DataFrame(
    [[99, 89, 100],
        [91, 98, 90],
        [100, 97, 85],
        [83, 100, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)
print(df)
# df_copy = df.iloc[:, [0, 2]]
# df_copy = df.loc[:, ['KOR', 'MAT']]
df_copy = df.loc[:, 'KOR':'MAT':2]
# 1번 학생의 수학 성적(100) 출력
print(df.at[1, 'MAT'])
#print(df.iat[1, 3])
print(df.iat[0, 2])
# 국어, 수학 칼럼을 추출
# 조건은 국어 성적이 95점 이상인 경우
df_copy = df.loc[df['KOR']>=95, ['KOR', 'MAT']]
print(df_copy)

df = (pd.melt(df)
       .rename(columns={
        'variable': 'subject',
        'value': 'score'})
       .query('score >= 90')
       .sort_values('score', ascending=False)
       )
print(df)
print(df.iloc[:, [1]])