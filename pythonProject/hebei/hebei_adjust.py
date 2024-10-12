import os
import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
path = r"C:\Users\John\Desktop\join.xlsx"
df = pd.read_excel(path)
df = df.dropna(axis=0, how='all')
df = df.dropna(axis=0, thresh=2)
df = df.reset_index(drop=True)
lst = []
for i in range(len(df)):
    tlst = df.iloc[i].tolist()
    for j in tlst:
        if pd.isnull(j):
            tlst.remove(j)
    lst.append(tlst)
df1 = pd.DataFrame(lst)
df1 = df1[[0, 1, 2, 3, 4]]
df1 = df1.dropna(axis=0, how='all')
df1 = df1.reset_index(drop=True)
print(str(2021) in str(df1.loc[0, 0]))
j = "1"  # j为备份指针,指向当前年份行
for i in range(len(df1)):
    if str(2023) in str(df1.loc[i, 0]):
        j = "2023"
        continue
    elif (str(2022) in str(df1.loc[i, 0])) | (str(2021) in str(df1.loc[i, 0])):
        j = "0"
        df1 = df1.drop(i)
        continue
    if j == "2023":
        continue
    elif j == "0":
        df1 = df1.drop(i)
df1 = df1.reset_index(drop=True)
df1.to_excel(r"C:\Users\John\Desktop\join1.xlsx", index=False)

# path = r"D:\pic\hebei2024\join.xlsx"
# df = pd.read_excel(path)
print()


