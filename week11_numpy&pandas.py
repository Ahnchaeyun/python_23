# import pandas as pd
#
# df1 = pd.DataFrame(
#     {
#         "KOR": [99, 91, 100],
#         "ENG": [89, 98, 97],
#         "MAT": [100, 90, 85],
#     }, index=[1, 2, 3]
# )
# print(df1)
#
# df2 = pd.DataFrame(
#     [[99, 89, 100],
#         [91, 98, 90],
#         [100, 97, 85]],
#     index=[1, 2, 3],
#     columns=['KOR', 'ENG', 'MAT']
# )
# print(df2)

# import pandas as pd
# df1 = pd.DataFrame(
#     {
#         "KOR": [99, 91, 100],
#         "ENG": [89, 98, 97],
#         "MAT": [100, 90, 85],
#     }, index=[1, 2, 3]
# )
# # print(df1)
#
# df2 = pd.DataFrame(
#     [[99, 89, 100],
# @@ -16,4 +16,14 @@
#     index=[1, 2, 3],
#     columns=['KOR', 'ENG', 'MAT']
# )
# print(df2)
# df2 = (pd.melt(df2)
#        .rename(columns={
#         'variable': 'subject',
#         'value': 'score'})
#        .query('score >= 90')
#        )
#
# print(df2)

# import pandas as pd
# df1 = pd.DataFrame(
#     {
#         "KOR": [99, 91, 100],
#         "ENG": [89, 98, 97],
#         "MAT": [100, 90, 85],
#     }, index=[1, 2, 3]
# )
# print(df1)
# print(df1.sort_values('MAT'))
#
# df2 = pd.DataFrame(
#     [[99, 89, 100],
#         [91, 98, 90],
#         [100, 97, 85]],
#     index=[1, 2, 3],
#     columns=['KOR', 'ENG', 'MAT']
# )
# print(df2)
# df2 = (pd.melt(df2)
#        .rename(columns={
#         'variable': 'subject',
#         'value': 'score'})
#        .query('score >= 90')
#        .sort_values('score', ascending=False)
#        )
#
# print(df2)

# import pandas as pd
# df1 = pd.DataFrame(
#     {
#         "KOR": [99, 91, 100],
#         "ENG": [89, 98, 97],
#         "MAT": [100, 90, 85],
#     }, index=[1, 2, 3]
# )
# print(df1)
# print(df1.sort_values('MAT'))
# df1 = df1.drop(columns=['ENG'])
# print(df1)
#
# df2 = pd.DataFrame(
#     [[99, 89, 100],
#         [91, 98, 90],
#         [100, 97, 85]],
#     index=[1, 2, 3],
#     columns=['KOR', 'ENG', 'MAT']
# )
# print(df2)
# df2 = (pd.melt(df2)
#        .rename(columns={
#         'variable': 'subject',
#         'value': 'score'})
#        .query('score >= 90')
#        .sort_values('score', ascending=False)
#        )
# print(df2)

# import pandas as pd
# df = pd.DataFrame(
#     [[99, 89, 100],
#         [91, 98, 90],
#         [100, 97, 85],
#         [83, 100, 94]],
#     index=[1, 2, 3, 4],
#     columns=['KOR', 'ENG', 'MAT']
# )
# print(df)
# # df_copy = df.iloc[:, [0, 2]]
# # df_copy = df.loc[:, ['KOR', 'MAT']]
# df_copy = df.loc[:, 'KOR':'MAT':2]
# print(df_copy)
#
# df = (pd.melt(df)
#        .rename(columns={
#         'variable': 'subject',
#         'value': 'score'})
#        .query('score >= 90')
#        .sort_values('score', ascending=False)
#        )
#
# print(df)
# print(df.iloc[:, [1]])





