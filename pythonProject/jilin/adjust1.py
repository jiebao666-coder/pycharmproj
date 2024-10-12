import os
import re

import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
path = r"C:\Users\John\Desktop\文史类adjust.xlsx"

# sheet list:理工农医类提前批、理工农医类国家专项计划批、理工农医类第一批、理工农医类地方专项计划批、理工农医类第二批
# sheet list:文史提前批、文史类国家专项计划批、文史类第一批、文史地方专项计划批、文史类第二批

df = pd.read_excel(path, sheet_name="文史类第二批")

for i in range(len(df)):
    df.iloc[i]["录取院校及专业"] = ''.join(str(df.iloc[i]["录取院校及专业"]).split(' '))
for i in range(len(df)):
    if (str("大学") in str(df.loc[i, '录取院校及专业'])) or (str("学院") in str(df.loc[i, '录取院校及专业'])) or (str("学校") in str(df.loc[i, '录取院校及专业'])):
        df.loc[i, "院校"] = df.loc[i, '录取院校及专业']
df["分数"] = df["录取总人数"].str.extract(r"\((.*)\)")[0]
# df = df.reset_index(drop=True)
for i in range(len(df)):
    try:
      df.loc[i, "录取人数"] = int(re.sub(r'\([^)]*\)', '', str(df.loc[i, "录取总人数"])))
    except Exception as e:
        print('An IndexError occurred:', i+2)
    lst = str(df.iloc[i]["分数"]).split('/')
    try:
        df.loc[i, "最高分"] = int(lst[0])
        df.loc[i, "最低分"] = int(lst[1])
    except IndexError as e:
        print('An IndexError occurred:', i+2)
    except Exception as e:
        print('An IndexError occurred:', i+2)

del df["录取总人数"]
del df["分数"]
# excel name:理工类提前批、理工类国家专项计划批、理工类第一批、理工类地方专项计划批、理工类第二批
# excel name:文史提前批、文史类国家专项计划批、文史类第一批、文史地方专项计划批、文史类第二批
df.to_excel(r"C:\Users\John\Desktop\文史类第二批.xlsx", index=False)
