import os
import re

import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


# sheet list:理工农医类提前批、理工农医类国家专项计划批、理工农医类第一批、理工农医类地方专项计划批、理工农医类第二批
# sheet list:文史提前批、文史类国家专项计划批、文史类第一批、文史地方专项计划批、文史类第二批
# excel name:理工类提前批、理工类国家专项计划批、理工类第一批、理工类地方专项计划批、理工类第二批
lst_name = ["文史提前批", "文史类国家专项计划批", "文史类第一批", "文史地方专项计划批", "文史类第二批",
            "理工类提前批", "理工类国家专项计划批", "理工类第一批", "理工类地方专项计划批", "理工类第二批"]
for j in range(len(lst_name)):
    path = r"C:\Users\John\Desktop\{}.xlsx".format(lst_name[j])
    df = pd.read_excel(path)
    # 检查录取人数和分数
    # lst = []
    # for i in range(len(df)):
    #     lst.append(df.iloc[i].tolist())
    #
    # for i in range(len(lst)):
    #     if not pd.isnull(df.loc[i, "院校"]):
    #         sum = lst[i][2]
    #         sum_temp = 0  # 当前学校temp人数和
    #     else:
    #         sum_temp += lst[i][2]
    #     if (i == len(lst) - 1) or (not pd.isnull(df.loc[i+1, "院校"])):
    #         if sum_temp != sum:
    #             lst[i].append("有问题")
    #             print(lst_name[j], "中，第", i+2, "行有问题")
    # if df.loc[i, "录取人数"] == 1:
    #     if df.loc[i, "最高分"] != df.loc[i, "最低分"]:
    #         print("2:", i + 1, "行有问题")

    # df1 = pd.DataFrame(lst)

    # for i in range(len(df)):
    #     if not pd.isnull(df.loc[i, "院校"]):
    #         num_max = df.loc[i, "最高分"]
    #         num_min = df.loc[i, "最低分"]
    #     elif (df.loc[i, "最高分"] > num_max) or (df.loc[i, "最低分"] < num_min):
    #         print(lst_name[j], "中，第", i+2, "行有问题")

    for i in range(len(df)):
        if not pd.isnull(df.loc[i, "院校"]):
            t = df.loc[i, "院校"]
            df = df.drop(i)
        else:
            try:
                df.loc[i, "院校"] = t
            except ValueError:
                print(df.loc[i, "院校"], "有问题")
    df = df.reset_index(drop=True)
    df.to_excel(r"C:\Users\John\Desktop\{}{}.xlsx".format(lst_name[j], "_checked"), index=False)

