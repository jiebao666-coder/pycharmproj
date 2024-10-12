import os
import re

import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
# 读文件
path = r"D:\pic\henan2023\result_adj2.xlsx"
df = pd.read_excel(path, header=None)

# df1 = pd.to_numeric(df.loc[1:, 2])
# df2 = pd.to_numeric(df.loc[1:, 3])
# df[2]=df1
# df[3]=df2
# df3 = df.loc[(df[2] != df[3])]
# print()

# 去除年份和学校代码
for i in range(1, len(df)):  # i为工作指针
    str1 = ""
    if not pd.isnull(df.loc[i, 0]):
        lst = list(str(df.loc[i, 0]))[4:]
        str1 = ''.join(lst)
    if str1 is not None:
        df.loc[i, 0] = str(str1)
df[0][0] = "学校名称"

#  将院校填充到每个具体专业前面
j = ""  # 指向当前学校行
for i in range(1, len(df)):  # i为工作指针
    # tips：这里是空值判断（“”），不是nan或None
    if df.loc[i, 0] != "":
        j = df.loc[i, 0]
        df = df.drop(i)
        continue
    if df.loc[i, 0] == "":
        df.loc[i, 0] = j
        continue
df = df.reset_index(drop=True)
# 添加“批次”和“文理艺体”列
lst1 = list()
lst2 = list()
lst1.append("文理艺体")
lst2.append("批次")
for i in range(1, len(df)):
    lst1.append("文科")
    lst2.append("本科一批")
df.insert(loc=2, column=len(df.columns), value=lst1)
df.insert(loc=2, column=len(df.columns), value=lst2)
df.columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = df[1].str.extract(r"(\(.*\))")[0].tolist()
lst[0] = "备注"
df[9] = lst
for i in range(1, len(df)):
    school = df.loc[i, 1]
    df.loc[i, 1] = re.sub(r'\([^)]*\)', '', str(df.loc[i, 1]))
# df[1] = df[1].str.replace(r"\(.*\)", "")
df.to_excel(r"D:\pic\henan2023\result_adj3.xlsx", index=False, header=False)

print()

