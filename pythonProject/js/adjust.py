import os
import re

import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
lst_name = ["江苏本科历史科目", "江苏本科物理科目", "江苏本科体育", "江苏艺术历史科目", "江苏艺术物理科目"]
for k in lst_name:
    path = r"C:\Users\John\Desktop\{}1.xlsx".format(k)
    df = pd.read_excel(path)
    df1 = df
    for i in range(len(df1)):
        if bool(re.match(r'^\d{4}', df.loc[i, 0])):
            sch = df.loc[i, 0]
            df = df.drop(i)
        elif sch != None:
            df.loc[i, 5] = str(sch)

        if (i == len(df1) - 1) or bool(re.match(r'^\d{4}', df.loc[i + 1, 0])):
            sch = None
    df.reset_index(drop=True, inplace=True)
    lst = []
    for i in range(len(df)):
        lst.append(df.iloc[i].tolist())

    for i in range(len(lst)):
        if bool(re.match(r'^\d{2}', df.loc[i, 0])):
            sum = lst[i][1]
            sum_temp = 0  # 当前学校temp人数和
        else:
            sum_temp += lst[i][1]
        if (i == len(lst)-1) or bool(re.match(r'^\d{2}', df.loc[i+1, 0])):
            if sum_temp != sum:
                lst[i].append("有问题")
    df2 = pd.DataFrame(lst)
    path1 = r"C:\Users\John\Desktop\{}2.xlsx".format(k)
    df2.to_excel(path1, index=False)
