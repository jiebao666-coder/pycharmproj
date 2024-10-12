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
    path = r"C:\Users\John\Desktop\{}2.xlsx".format(k)
    df = pd.read_excel(path)
    df1 = df
    opt = None
    tip = None
    for i in range(len(df1)):
        if bool(re.match(r'^\d{2}', df.loc[i, 0])):
            try:
                opt = match(df.loc[i, 0])[0]
                if len(match(df.loc[i, 0])) > 1:
                    t = match(df.loc[i, 0])
                    t.pop(0)
                    tip = "".join(t)
                df = df.drop(i)
            except IndexError as e:
                print('An IndexError occurred:', i)

        elif opt != None:
            df.loc[i, 6] = str(opt)
            if not pd.isnull(tip):
                df.loc[i, 7] = str(tip)

        if (i == len(df1) - 1) or bool(re.match(r'^\d{2}', df.loc[i + 1, 0])):
            opt = None
            tip = None
    df.reset_index(drop=True, inplace=True)
    df.to_excel(r"C:\Users\John\Desktop\{}3.xlsx".format(k), index=False)
