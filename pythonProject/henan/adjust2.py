import os
import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
# 读文件
path = r"D:\pic\henan2023\henan2023-check\result_adj1.xlsx"
df = pd.read_excel(path)
j = 0  # j为备份指针,指向当前年份行
for i in range(1, len(df)):  # i为工作指针
    if df.loc[i, 1] == 2023:
        j = df.loc[i, 1]
        continue
    if j == 2023 & pd.isnull(df.loc[i, 1]):
        continue
    if (df.loc[i, 1] == 2022) | (df.loc[i, 1] == 2021):
        j = df.loc[i, 1]
        df = df.drop(i)
        continue
    if ((j == 2022) | (j == 2021)) & pd.isnull(df.loc[i, 1]):
        df = df.drop(i)

df.to_excel(r"D:\pic\henan2023\henan2023-check\result2.xlsx", index=False)


