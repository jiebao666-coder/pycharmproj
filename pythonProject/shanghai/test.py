import os
import re
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
class forrange:
    def __init__(self, startOrStop, stop=None, step=1):
        if step == 0:
            raise ValueError('forrange step argument must not be zero')
        if not isinstance(startOrStop, int):
            raise TypeError('forrange startOrStop argument must be an int')
        if stop is not None and not isinstance(stop, int):
            raise TypeError('forrange stop argument must be an int')

        if stop is None:
            self.start = 0
            self.stop = startOrStop
            self.step = step
        else:
            self.start = startOrStop
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self.foriterator(self.start, self.stop, self.step)

    class foriterator:

        def __init__(self, start, stop, step):
            self.currentValue = None
            self.nextValue = start
            self.stop = stop
            self.step = step

        def __iter__(self): return self

        def next(self):
            if self.step > 0 and self.nextValue >= self.stop:
                raise StopIteration
            if self.step < 0 and self.nextValue <= self.stop:
                raise StopIteration
            self.currentValue = forrange.forvalue(self.nextValue, self)
            self.nextValue += self.step
            return self.currentValue

    class forvalue(int):
        def __new__(cls, value, iterator):
            value = super(forrange.forvalue, cls).__new__(cls, value)
            value.iterator = iterator
            return value

        def update(self, value):
            if not isinstance(self, int):
                raise TypeError('forvalue.update value must be an int')
            if self == self.iterator.currentValue:
                self.iterator.nextValue = value + self.iterator.step

path = r"C:\Users\John\Desktop\理工结果.xlsx"
df = pd.read_excel(path)

# 不成功，边删除边遍历版
# for j in forrange(len(df)):
#     try:
#         if (str("大学") in str(df.loc[j, 0])) or (str("学院") in str(df.loc[j, 0])) or (str("学校") in str(df.loc[j, 0])):
#             if str("院校简称") in str(df.loc[j, 0]):
#                 t = df.loc[j, 0]
#                 # df = df.drop(i)
#                 df = df.drop(j+1)
#                 df = df.drop(j+2)
#                 j.update(j + 2)
#             else:
#                 t = df.loc[j, 0]
#                 # df = df.drop(i)
#                 df = df.drop(j+1)
#                 j.update(j + 1)
#
#         if j >= len(df)-1:
#             break
#     except Exception as e:
#         print(str(e))

# 合并意外换行的字符串
# j = 1
# for i in range(1, len(df)):
#     t = df.loc[j].tolist()[1:]
#     df1 = pd.DataFrame(t)
#     if j >= len(df)-1:
#         break
#     try:
#         if len(t) - df1[0].isnull().sum() == 1:
#             df.loc[j-1, 2] = str(df.loc[j-1, 2])+str(df.loc[j, 2])
#             df.drop(j)
#         j = j + 1
#     except ValueError as e:
#         print(e)
#     except TypeError as e:
#         print(e)

# 删除一些多余行
# j = 0
# while True:
#     try:
#         if (str("大学") in str(df.loc[j, 0])) or (str("学院") in str(df.loc[j, 0])) or (str("学校") in str(df.loc[j, 0])):
#             if str("院校简称") in str(df.loc[j+1, 0]):
#                 t = df.loc[j, 0]
#                 # df = df.drop(i)
#                 df = df.drop(j+1)
#                 df = df.drop(j+2)
#                 j = j + 2
#             else:
#                 t = df.loc[j, 0]
#                 # df = df.drop(i)
#                 df = df.drop(j+1)
#                 j = j + 1
#         j = j + 1
#         if j >= len(df)-1:
#             break
#     except Exception as e:
#         print(str(e))

# 查总录取人数错误
# lst = []
# for i in range(len(df)):
#     lst.append(df.iloc[i].tolist())
#
# for i in range(len(lst)):
#     if not pd.isnull(lst[i][1]):
#         sum = lst[i][3]
#         sum_temp = 0  # 当前学校temp人数和
#     else:
#         sum_temp += lst[i][3]
#     if (i == len(lst)-1) or (not pd.isnull(lst[i + 1][1])):
#         if sum_temp != sum:
#             lst[i].append("有问题")
# df1 = pd.DataFrame(lst)


# lst = []
# for i in range(len(df)):
#     lst.append(df.iloc[i].tolist())
#
# for i in range(len(lst)):
#     if lst[i][4] == "按学校录取规则折算":
#         continue
#     if not pd.isnull(lst[i][1]):
#         minn = lst[i][4]
#     else:
#         if lst[i][4] < minn:
#             lst[i].append("有问题")

# df1 = pd.DataFrame(lst)

# for i in range(len(df)):
#     if (str(df.loc[i, "专业"])[-1] == "类") or (str(df.loc[i, "专业"])[-1] == "班"):
#         if "、" in str(df.loc[i, "专业备注1"]) and str(df.loc[i, "专业备注1"])[-2] != "等":
#             df.loc[i, "专业备注"] = df.loc[i, "专业备注1"]
#             df.loc[i, "专业备注1"] = np.nan
for i in range(len(df)):
    if pd.isnull(df.loc[i, "最高分"]):
        df.drop(i, axis=0, inplace=True)
df.reset_index(drop=True)

df.to_excel(r"C:\Users\John\Desktop\理工结果1.xlsx", index=False)
