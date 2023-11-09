import pandas as pd
df = pd.DataFrame(
    [[99, 89, 81],
        [91, 98, 90],
        [95, 97, 85],
        [83, 96, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)

print(df)
df = df.apply(lambda n: n + 1)

df = [[99, 89, 81], [91, 98, 90], [95, 97, 85], [83, 96, 94]]
index = [1, 2, 3, 4]
columns = ['KOR', 'ENG', 'MAT']

for j in columns:
    print(j , end = ' ')
print("\t")
for i in range(len(df)):
    print(f"{index[i]}   {df[i][0]}   {df[i][1]}   {df[i][2]}")

# for c in columns:
#     print(c, end = ' ')
# print(' ')
# for row in range(4):
#     for col in range(3):
#         print(df[row][col, end=' '])




