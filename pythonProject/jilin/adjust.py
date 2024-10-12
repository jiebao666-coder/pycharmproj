import os
import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
path = r"D:\pic\jilin2023\理工类.xlsx"
df = pd.read_excel(path, header=None)
df = df.dropna(axis=0, how='all')
df = df.reset_index(drop=True)
t = list()
j = 0
for i in range(1, len(df)):
    if pd.isnull(df.loc[i, 1]):
        t[j-1][0] = str(df.loc[i-1, 0])+str(df.loc[i, 0])
        df.drop(i)
    else:
        t.append(df.loc[i].tolist())
        j = j+1
df1 = pd.DataFrame(t)
path1 = r'C:\Users\John\Desktop\理工类.xlsx'    # 结果保存位置
df1.to_excel(path1, index=False)



