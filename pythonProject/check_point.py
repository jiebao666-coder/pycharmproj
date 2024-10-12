import pandas as pd
import numpy as np
import re
import os
import openpyxl
import warnings

warnings.filterwarnings('ignore')
path = r"D:\pic\hebei2024\提前批.xlsx"
df = pd.read_excel(path, header=None)
df.columns = ["学校", "录取人数", "最高分", "最低分", "平均分", "批次"]
for i in range(1, len(df)):
    if (df.loc[i, "平均分"] > df.loc[i, "最高分"]) | (df.loc[i, "平均分"] < df.loc[i, "最低分"]):
        print("1:", i + 1, "行有问题")
    if df.loc[i, "录取人数"] == 1:
        if df.loc[i, "最高分"] != df.loc[i, "最低分"]:
            print("2:", i + 1, "行有问题")
    if df.loc[i, "录取人数"] == 2:
        # if df.loc[i, "最高分"] + df.loc[i, "最低分"] != df.loc[i, "平均分"] * 2:
        #     print(i + 2, "行有问题")
        if abs(((df.loc[i, "最高分"] + df.loc[i, "最低分"])/2)-df.loc[i, "平均分"]) >= 1:
            print("3:", i + 1, "行有问题")

    # 注意浮点数问题
    # if df.loc[i, "录取人数"] == 3:
    #     if round(abs(((df.loc[i, "最高分"] + df.loc[i, "最低分"])/2)-df.loc[i, "平均分"]),0) > round((df.loc[i, "最高分"] - df.loc[i, "最低分"])/6,1):
    #         print(i + 2, "行有问题")
    if df.loc[i, "最高分"]-df.loc[i, "最低分"] > 1:
        if ((df.loc[i, "平均分"] == df.loc[i, "最高分"]) | (df.loc[i, "平均分"] == df.loc[i, "最低分"])) & (df.loc[i, "录取人数"] > 3):
            print(i+1)

# path1 = r'D:\pic\henan2023\henan2023-check\sch_maj_cut.xlsx'
# df1 = pd.read_excel(path, sheet_name='Sheet1')

# # 核对公布人数
# df_1 = df.groupby("院校")["公布计划"].sum().reset_index()
# df1_1 = df1.groupby("院校")["公布计划"].sum().reset_index()
# for i in range(0, len(df_1)):
#     if df_1.loc[i]["公布计划"] != df1_1.loc[i]["公布计划"]:
#         print(df_1.loc[i]) # print(df_1.loc[i])
#     # else: print(df_1.loc[i]["公布计划"], " = ", df1_1.loc[i]["公布计划"])
#
# lst=list()
# for i in range(0, len(df)):
#     if df.loc[i]["公布计划"] != df.loc[i]["录取人数"]:
#         print(i)
#         lst.append(df.loc[i][["院校", "专业", "公布计划", "录取人数"]])
# df3 = pd.DataFrame(lst)
