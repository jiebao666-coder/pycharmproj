import os
import re
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
lst_name = ["江苏本科历史科目", "江苏本科物理科目", "江苏本科体育", "江苏艺术历史科目", "江苏艺术物理科目"]
# for k in lst_name:
#     path = r"D:\pic\js2023\{}2.xlsx".format(k)
#     df = pd.read_excel(path)
#     max = 0
#     min = 0
#     print(k)
#     for i in range(len(df)):
#         if bool(re.match(r'^\d{2}', df.loc[i, 0])):
#             # print(df.loc[i, 0])
#             max = df.loc[i, 2]
#             min = df.loc[i, 3]
#         elif (df.loc[i, 2] > max) or (df.loc[i, 3] < min):
#             print(i + 2)
lst_pd = []
for i in lst_name:
    path = r"D:\pic\js2023\{}.xlsx".format(i)  # 你的表
    lst_pd.append(pd.read_excel(path))
out = pd.concat(lst_pd)
out.to_excel(r'C:\Users\John\Desktop\江苏源数据.xlsx', index=False)