import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()  # an empty figure with no Axes
# fig, ax = plt.subplots()  # a figure with a single Axes

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out



# df = pd.DataFrame({
# 'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
# 'population': [17.04, 143.5, 9.5, 45.5],
# 'square': [2724902, 17125191, 207600, 603628]
# })
# # print(df)

# print(df)


# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo",
#     }
# )

# print(df2.describe)

# x = [4,9,16,25,36]
# fig = plt.figure(figsize=(9, 5))
# plt.pie(x, labels=("Hello", "Darkness", "My", "Old", "Friend"), 
#         colors = ("#30D5C8", "#2F35E9", "#D220CD", "#E7FF12", "#2E7B80"))
# plt.show()

# X = ["02.09", "04.09", "06.09", "08.09", "10.09", "12.09", "14.09", "16.09", "18.09", "20.09", "22.09", "24.09", "26.09", "28.09", "30.09"]
# Y = [32,36,39,52,61,72,77,75,68,57,48,48, 30, 23, 45]
# fig, ax = plt.subplots()
# ax.plot(X, Y)
# # plt.scatter(X, Y, s=60, c='red', marker='^')
# plt.title('New Users')
# plt.xlabel('Day')
# plt.ylabel('Users per day')
# plt.xlim(0,31)
# plt.ylim(0,80)
# plt.show()
