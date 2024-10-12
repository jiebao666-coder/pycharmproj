import os
import re

import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
path = r"D:\pic\hebei2024\本科批.xlsx"
df = pd.read_excel(path)
df.columns = ["专业", "录取人数", "最高分", "最低分", "平均分", "批次"]
df["院校"] = np.nan
sch = None
df1 = df
for i in range(len(df1)):
    if bool(re.match(r'^\d\d\d\d', df.loc[i, "专业"])):
        sch = df.loc[i, "专业"]
        df = df.drop(i)
    elif sch != None:
        df.loc[i, "院校"] = str(sch)[4:]
        df.loc[i, "专业"] = str(df.loc[i, "专业"])[2:]

    if (i == len(df1) - 1) or bool(re.match(r'^\d\d\d\d', df.loc[i + 1, "专业"])):
        sch = None
df.to_excel(r"C:\Users\John\Desktop\本科批check.xlsx", index=False)
print()

