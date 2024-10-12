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


lst_name = ["江苏本科历史科目", "江苏本科物理科目", "江苏本科体育", "江苏艺术历史科目", "江苏艺术物理科目"]
for k in lst_name:
    path = r"C:\Users\John\Desktop\{}（匹配）.xlsx".format(k)
    df = pd.read_excel(path)
    lst_str = []
    t_str = ""
    for i in range(len(df)):
        lst_str.append(df.loc[i, "选科要求1"])
        if "不限" in str(df.loc[i, "选科要求"]):
            try:
                t = "、".join(lst_str)
            except TypeError:
                print(k, ":", i)
            lst_str.clear()
        else:
            t_str = str(df.loc[i, "选科要求"])
            t_str = t_str[1:len(t_str)-1]
            t_str = t_str.replace("或", "/")
            t_str = t_str.replace("和", "、")
            lst_str.append(t_str)
            t = "、".join(lst_str)
            lst_str.clear()
        df.loc[i, "选科"] = t

    lst_bz = []
    lst_t = []
    lst_t1 = []
    for i in range(len(df)):
        if pd.isnull(df.loc[i, "专业备注1"]):
            continue
        else:
            if ("类" in df.loc[i, "专业"]) or ("班" in df.loc[i, "专业"]):
                lst_bz = match(df.loc[i, "专业备注1"])
                for j in lst_bz:
                    if ("、" in j) and ("等" not in j):
                        lst_t.append(j)
                    else:
                        lst_t1.append(j)
                df.loc[i, "专业备注"] = ''.join(lst_t)
                df.loc[i, "专业备注1"] = ''.join(lst_t1)
            lst_t.clear()
            lst_t1.clear()
            lst_bz.clear()
    df.to_excel(r"C:\Users\John\Desktop\{}结果.xlsx".format(k), index=False)


