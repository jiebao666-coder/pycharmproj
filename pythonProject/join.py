import os
from time import sleep

import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


def sheet_join(file_num, del_raw):
    path = r"C:\Users\John\Desktop\result{}.xlsx".format(file_num)
    # path_file = path+"\\"+file
    df2 = pd.ExcelFile(path)
    sheet_lst = df2.sheet_names
    df_lst = []

    for sheet in sheet_lst:
        df1 = pd.read_excel(path, sheet_name=sheet, header=None)
        df_lst.append(df1)
    lst = list(range(del_raw))
    df = pd.concat(df_lst)
    df = df.reset_index(drop=True)

    df = df.dropna(axis=0, how='all')
    df = df.dropna(axis=1, how='all')
    df = df.reset_index(drop=True)

    lst.append(len(df)-1)

    df = df.drop(df.index[lst])
    df = df.reset_index(drop=True)
    # pd.concat(dfs).to_excel("text1.xlsx")
    # print(df)
    df = df.dropna(axis=1, how='all')
    df = df.reset_index(drop=True)
    return df


if __name__ == '__main__':
    # debug看一下pandas结构确定这两个参数，是指需要删除的顶部多余行
    firstPage_delraw = 0
    restPage_delraw = 1

    path = r"C:\Users\John\Desktop"  # 输入文件夹地址
    files = os.listdir(path)  # 读入文件夹
    num_files = len(files)
    xlsx_list = []
    # xlsx_list.append(sheet_join(1, firstPage_delraw))
    for i in range(1, 32):
        xlsx_list.append(sheet_join(i, restPage_delraw))
    print()
    result = pd.concat(xlsx_list)
    result = result.reset_index(drop=True)
    # 删除空白行
    result = result.dropna(axis=0, how='all')
    result = result.reset_index(drop=True)
    # result.flush()
    # result.close()
    result.to_excel(r"C:\Users\John\Desktop\join.xlsx", index=False)


