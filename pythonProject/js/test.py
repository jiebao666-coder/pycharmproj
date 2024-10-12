import os
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
lst_name = ["江苏本科历史科目", "江苏本科物理科目", "江苏本科体育", "江苏艺术历史科目", "江苏艺术物理科目"]
# for k in lst_name:
#     path = r"C:\Users\John\Desktop\{}.xlsx".format(k)
#     df = pd.read_excel(path, header=None)
#     df.dropna(axis=0, how='all', inplace=True)
#     df.dropna(axis=0, thresh=2, inplace=True)
#     df.reset_index(drop=True, inplace=True)
#     for i in range(0, len(df)):
#         if "院校" in str(df.loc[i, 0]):
#             df.drop(i, axis=0, inplace=True)
#     df.reset_index(drop=True, inplace=True)
#     for j in range(len(df)):
#         if pd.isnull(df.loc[j, 0]):
#             continue
#         else:
#             tlst = list(df.loc[j, 0])
#             for i in tlst:
#                 if pd.isnull(i) or i == ' ':
#                     tlst.remove(i)
#             df.loc[j, 0] = ''.join(tlst)
#     df.to_excel(r"C:\Users\John\Desktop\{}1.xlsx".format(k), index=False)


