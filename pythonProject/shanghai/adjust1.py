import os
import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
path = r"C:\Users\John\Desktop\本科普通批test1.xlsx"
df = pd.read_excel(path)
df = df.dropna(axis=0, how='all')
df = df.reset_index(drop=True)

# 院校名提取+删除空格
# tlst = []
# for i in range(len(df)):
#     if not pd.isnull(df.loc[i, "院校"]):
#         df.loc[i, "院校"] = str(df.loc[i, "院校"]).split(' ')[0]
# for j in range(len(df)):
#     if pd.isnull(df.loc[j, "专业"]):
#         continue
#     else:
#         tlst = list(df.loc[j, "专业"])
#         for i in tlst:
#             if pd.isnull(i) or i == ' ':
#                 tlst.remove(i)
#         df.loc[j, "专业"] = ''.join(tlst)
#
# tlst = []
# for j in range(len(df)):
#     if pd.isnull(df.loc[j, "备注"]):
#         continue
#     else:
#         tlst = list(df.loc[j, "备注"])
#         for i in tlst:
#             if pd.isnull(i) or i == ' ':
#                 tlst.remove(i)
#         df.loc[j, "备注"] = ''.join(tlst)


# 学校名赋值
# j = ""  # 指向当前学校行
# lst = []
# for i in range(0, len(df)):  # i为工作指针
#     lst = df.loc[i].tolist()
#     if np.sum(~pd.isnull(lst)) == 1:
#         j = df.loc[i, "院校"]
#         df = df.drop(i)
#         continue
#     else:
#         df.loc[i, "院校"] = j

j = ""  # 指向当前专业组行
lst = []
for i in range(0, len(df)):  # i为工作指针
    lst = df.loc[i].tolist()
    if not pd.isnull(lst[1]):
        j = df.loc[i, 1]
        df = df.drop(i)
        continue
    else:
        df.loc[i, 1] = j

df = df.reset_index(drop=True)
df.to_excel(r"C:\Users\John\Desktop\本科普通批test2.xlsx", index=False)