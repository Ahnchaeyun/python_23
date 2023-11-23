import pandas as pd

d = pd.DataFrame(
    [['persian', 'bengal', 'russian'],
        ['maltese', 'poodle', 'retriever'],
        ['maltese', 7, 'cute']],
    index=['cat', 'dog', 'som'],
    columns=[1, 2, 3]
)
print(d)
print("-------------------")

data = {
    'A': [99, 89, 81],
    'B':[91, 98, 90],
    'C':[95, 97, 85]
}

dd = pd.DataFrame(data)
print(dd)

value = dd[1:4] #인덱스 1에서 3까지의 행

print(value)
print("-------------------")

df = pd.DataFrame(
    [[99, 89, 81],
        [91, 98, 90],
        [95, 97, 85],
        [83, 96, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)

data1 = df.loc[1:2] #1부터 2까지의 행
data2 = df.iloc[1:4] # 정수/1부터 3까지의 행

print(data1)
print(data2)

#apply: 특정함수 적용