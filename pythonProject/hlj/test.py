import re
import numpy as np

import pandas as pd
path = r"D:\pic\hlj2023\理工.xlsx"
df = pd.read_excel(path, header=None)
df.dropna(axis=0, how='all', inplace=True)
df.dropna(axis=0, thresh=2, inplace=True)
df = df.reset_index(drop=True)
for i in range(len(df)):
    if ("学校" in str(df.loc[i, 0])) or ("高" in str(df.loc[i, 2])):
        df = df.drop(i)

df = df.reset_index(drop=True)
df.to_excel(r"C:\Users\John\Desktop\理工test.xlsx", index=False)
