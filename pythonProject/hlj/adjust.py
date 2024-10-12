import re
import numpy as np

import pandas as pd
path = r"C:\Users\John\Desktop\理工test.xlsx"
df = pd.read_excel(path)
for j in range(len(df)):
    if pd.isnull(df.loc[j, 1]):
        continue
    else:
        tlst = list(df.loc[j, 1])
        for i in tlst:
            if pd.isnull(i) or i == ' ':
                tlst.remove(i)
        df.loc[j, 1] = ''.join(tlst)
df.to_excel(r"C:\Users\John\Desktop\理工.xlsx", index=False)
