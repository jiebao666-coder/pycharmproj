import os
import re
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

def match(str1):  # 匹配最外层括号
    lst_match = []
    lst_mark = []
    result = []
    lst_str = list(str1)
    first = 0
    last = 0
    for i in range(len(lst_str)):
        if lst_str[i] == '（':
            lst_mark.append(lst_str[i])
            if lst_mark.count('（') == 1:
                first = i

        if lst_str[i] == '）':
            if lst_mark[len(lst_mark) - 1] == '（':
                if lst_mark.count('（') != 1:
                    lst_mark.pop(len(lst_mark) - 1)
                else:
                    last = i
                    if i != len(lst_str) - 1:
                        lst_match.append(lst_str[first:last + 1])
                    else:
                        lst_match.append(lst_str[first:])
                    lst_mark.pop(len(lst_mark) - 1)
    for i in range(len(lst_match)):
        result.append("".join(lst_match[i]))
    return result

# 合并
# sheet list:理工农医类提前批、理工农医类国家专项计划批、理工农医类第一批、理工农医类地方专项计划批、理工农医类第二批
# sheet list:文史提前批、文史类国家专项计划批、文史类第一批、文史地方专项计划批、文史类第二批
# excel name:理工类提前批、理工类国家专项计划批、理工类第一批、理工类地方专项计划批、理工类第二批
# lst_name = ["文史类提前批", "文史类国家专项计划批", "文史地方专项计划批", "文史类第一批", "文史类第二批",
#             "理工类提前批", "理工类国家专项计划批", "理工类地方专项计划批", "理工类第一批", "理工类第二批"]
# lst_pd = []
# for i in range(len(lst_name)):
#     path = r"C:\Users\John\Desktop\{}_check.xlsx".format(lst_name[i])  # 你的表
#     lst_pd.append(pd.read_excel(path))
# out = pd.concat(lst_pd)
# out.to_excel(r'C:\Users\John\Desktop\result.xlsx', index=False)

# 专业拆分
path = r"D:\pic\jilin2023\result.xlsx"  # 你的表
df = pd.read_excel(path)
for i in range(0, len(df)):
    if pd.isnull(df.loc[i, "专业备注1"]):
        continue
    try:
        lst = match(str(df.loc[i, "专业备注1"]))
    except IndexError as e:
        print('An IndexError occurred:', i + 2)

    if str('、') in str(df.loc[i, "专业备注1"]):
        if len(lst) == 1:
            df.loc[i, "专业备注"] = df.loc[i, "专业备注1"]
            df.loc[i, "专业备注1"] = np.nan
        else:
            try:
                df.loc[i, "专业备注"] = lst[1]
                lst.pop(1)
                df.loc[i, "专业备注1"] = ''.join(lst)
            except IndexError as e:
                print('An IndexError occurred:', i + 2)

path = r"D:\pic\jilin2023\2024吉林统计结果.xlsx"
df.to_excel(path, index=False)

# 正则表达式test
# str1 = "(会计学院)(会计学、财务管理(sdf)、Sdf(asdf))"
# str2 = re.findall(r'\([^)]*\)', str1)
# str3 = re.findall(r"\((.*?)\)", str1)
# str4 = re.sub(r"\((.*?)\)", "", str1)
# print(str2)
# # str3.pop(0)
# print(str3)
# print(''.join(str3))
# print(str4)



# test
# str1 = "(会计学院)(会计学、财务管理(sdf)、Sdf(asdf))(asd(asdf)sdf)(55uw)"
# lst = match(str1)
# print(lst)
