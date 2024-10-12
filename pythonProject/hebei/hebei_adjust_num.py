import os
import re

import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
path = r"C:\Users\John\Desktop\check.xlsx"
df = pd.read_excel(path)
# print(bool(re.match(r'^\d\d\d\d', df.loc[0, 0])))


lst = []
for i in range(len(df)):
    lst.append(df.iloc[i].tolist())

for i in range(len(lst)):
    if bool(re.match(r'^\d\d\d\d', df.loc[i, 0])):
        sum = lst[i][1]
        sum_temp = 0  # 当前学校temp人数和
    else:
        sum_temp += lst[i][1]
    if (i == len(lst)-1) or bool(re.match(r'^\d\d\d\d', df.loc[i+1, 0])):
        if sum_temp != sum:
            lst[i].append("有问题")
df1 = pd.DataFrame(lst)
df1.to_excel(r"C:\Users\John\Desktop\check1.xlsx", index=False)
print()


