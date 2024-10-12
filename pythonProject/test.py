import os
import re
import numpy as np
import openpyxl
import pandas as pd
# path2 = r'D:\pic\henan2023\schoolList0922.xlsx'  # 匹配校名表
# df2 = pd.read_excel(path2,sheet_name='Sheet1')
#
# # 从列表创建一维NumPy数组
# school_name = df2['学校']
# sch_len = [len(school_name[i]) for i in range(len(school_name))]
# sch_idx = np.array(sch_len).argsort().tolist()
# sch_idx.reverse()
# sch_inf = np.array(school_name)[sch_idx]
# text=np.array(school_name)
# print(text[[1,5,9,7,5]])

str1 = "俄语(国际)"
str2 = str1.replace(r'\([^)]*\)', "")
print(str2)
print(re.sub(r'\([^)]*\)', '', str1))

# path = r"C:\Users\John\Desktop\体育check.xlsx"
# df = pd.read_excel(path)
# print(str("一志愿") in str(df.loc[52, 0]) or str("征集志愿") in str(df.loc[52, 0]))
# print()
# for i in range(len(df)):
#     if df.loc[i, 0] == "院校及专业名称(2023年)":
#         if (str("征集志愿") not in str(df.loc[i+1, 0])) and (str("一志愿") not in str(df.loc[i+1, 0])):
#             print(i+2)
# print(bool(re.match(r'^\d\d\d\d', df.loc[0, 0])))

# ascii码记录:
# 数字:48-->'0'  57-->'9'
# 大写字母:65-->'A'  90-->'Z'
# 小写字母:97-->'a'  122-->'z'
# print(chr(88))  # 88: 输出'X'
# s = '59872'
# print(ord(s[3]))  # '7': 输出55
# t = pd.DataFrame({"id": [s], "text": [s]},columns=["id","text"])
# lst = [1,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
# print(pd.isnull(lst))
# lst_name = ["理工", "文史"]
# lst_pd = []
# for i in range(len(lst_name)):
#     path = r"D:\pic\hlj2023\{}识别版.xlsx".format(lst_name[i])  # 你的表
#     lst_pd.append(pd.read_excel(path))
# out = pd.concat(lst_pd)
# out.to_excel(r'C:\Users\John\Desktop\黑龙江源数据.xlsx', index=False)
#
print(bool(re.match(r'^\d{4}', "45电风扇")))
print(re.match(r'^\d{5}', "4587电风扇"))
