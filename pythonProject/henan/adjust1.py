import os
import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

path = r"D:\pic\henan2023\henan2023-check\result1.xlsx"

df = pd.read_excel(path, header=None)
del df[0]
del df[4]
del df[5]
del df[6]
del df[7]
del df[8]
del df[9]
del df[10]

#print(df.loc[0:2,[0,1]]) #第0行到第2行，第0列和第1列
df.columns = [0, 1, 2]
# df.rename(columns={"one":"nj","two":"bj"},inplace=True) #针对性修改列名
df.loc[2, 1] = "年份"
# df.loc[2, 1] = "专业名称"
df.loc[2, 2] = "公布计划"
df.loc[2, 0] = "院校名称"

df = df.drop(0)
df = df.drop(1)
df = df.reset_index(drop=True)
# df.loc[0, 7] = "备注"

df.to_excel(r"D:\pic\henan2023\henan2023-check\result_adj1.xlsx", index=False)

print()
