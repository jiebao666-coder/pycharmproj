import os
import re
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
path = r"C:\Users\John\Desktop\本科普通批adjust1.xlsx"
df = pd.read_excel(path)


df_lst = []
for i in range(0, len(df)):
    df_lst.append(df.loc[i].tolist())
for i in range(0, len(df_lst)):
    lst = []
    if not pd.isnull(df_lst[i][3]):
        lst = str(df_lst[i][3]).split(' ')
        if len(lst) == 1:
            continue
        for j in range(0, len(lst)-1):
            df_lst.insert(i+j+1, [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
        for j in range(0, len(lst)):
            df_lst[j+i][3] = lst[j]
df = pd.DataFrame(df_lst)

# 不需自动插入新数据行版
lst_num = [4, 5]
for k in lst_num:
    j = 0
    while True:
        try:
            if j == len(df) - 3:
                break
            if not pd.isnull(df.loc[j, k]):
                lst = str(df.loc[j, k]).split(' ')
                for i in range(len(lst)):
                    df.loc[j+i, k] = lst[i]
                j = j + len(lst) - 1
            j = j + 1

        except Exception as e:
            print(k, e)


df.to_excel(r"C:\Users\John\Desktop\本科普通批adjust2.xlsx", index=False)
# print(str(df.loc[4, 4]).split(' '))