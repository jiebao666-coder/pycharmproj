import os
import numpy as np
import openpyxl
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
path = r"C:\Users\John\Desktop\join1.xlsx"
df = pd.read_excel(path)
j = "0"
for i in range(len(df)):
    if str("一志愿") in str(df.loc[i, 0]):
        j = "一志愿"
        df.loc[i, 5] = "体育提前批+一志愿"
        df = df.drop(i)
        continue
    elif str("征集志愿") in str(df.loc[i, 0]):
        j = "征集志愿"
        df.loc[i, 5] = "体育提前批+征集志愿"
        df = df.drop(i)
    elif j == "一志愿":
        df.loc[i, 5] = "体育提前批+一志愿"
        continue
    elif j == "征集志愿":
        df.loc[i, 5] = "体育提前批+征集志愿"
        continue
df = df.reset_index(drop=True)

df.to_excel(r"C:\Users\John\Desktop\check.xlsx", index=False)

print()
