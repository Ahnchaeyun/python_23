import numpy as np

# df = np.array({
#     'a': [1, 2, np.nan, 4],
#     'b':[5, np.nan, 7, 8],
#     'c':[9, 10, 11, np.nan]
# })

data = np.array([
    [1, 5, 9],
    [2, np.nan, 10],
    [np.nan, 7, 11],
    [4, 8, np.nan]
])

print(data)

means = np.nanmean(data, axis=0)

for i in range(data.shape[1]):
    # print(i)

    #True, False 값을 갖는 배열 생성
    mask = np.isnan(data[:, i])
    # print(mask)

    data[mask, i] = means[i]

print(data)