import pandas as pd
import numpy as np
import re


def school_major_deal(df2, df3):  # 按字符串长度从大到小排序
    school_name = df2['学校']
    sch_len = [len(school_name[i]) for i in range(len(school_name))]
    sch_idx = np.array(sch_len).argsort().tolist()
    sch_idx.reverse()
    sch_inf = np.array(school_name)[sch_idx]

    major_name = df3['本科和高职专业目录名称']
    major_len = [len(major_name[i]) for i in range(len(major_name))]
    major_idx = np.array(major_len).argsort().tolist()
    major_idx.reverse()
    major_inf = np.array(major_name)[major_idx]
    return sch_inf, major_inf


def judge_cut(df, sch_inf, major_inf):
    result = []
    for i in range(len(df)):
        result.append(df.iloc[i].tolist())
        sch = df[4][i][4:]
        maj = df[0][i]
        # print(i, maj)
        if sch in sch_inf:
            result[-1].append(sch)
            result[-1].append('')
        if sch not in sch_inf:
            count = 0
            for sch1 in sch_inf:
                if sch1 in sch and sch.find(sch1) == 0:
                    bei_zhu = sch[len(sch1):]
                    result[-1].append(sch1)
                    result[-1].append(bei_zhu)
                    break
                count += 1
                if count == len(sch_inf):
                    result[-1].append('')
                    result[-1].append('有问题')
        if maj in major_inf:
            result[-1].append(maj)
            result[-1].append('')
        if maj not in major_inf:
            count = 0
            for ma in major_inf:
                if ma in maj and maj.find(ma) == 0:
                    bei_zhu = maj[len(ma):]
                    result[-1].append(ma)
                    result[-1].append(bei_zhu)
                    break
                count += 1
                if count == len(major_inf):
                    result[-1].append('')
                    result[-1].append('有问题')
    return result, df.columns.tolist() + ['院校切分', '院校备注', '专业切分', '专业备注1']


# sheet list:文史提前批、文史类国家专项计划批、文史类第一批、文史地方专项计划批、文史类第二批
# excel name:理工类提前批、理工类国家专项计划批、理工类第一批、理工类地方专项计划批、理工类第二批
lst_name = ["江苏本科历史科目", "江苏本科物理科目", "江苏本科体育", "江苏艺术历史科目", "江苏艺术物理科目"]
for k in lst_name:
    path1 = r"C:\Users\John\Desktop\{}3.xlsx".format(k)  # 你的表
    df1 = pd.read_excel(path1, sheet_name="Sheet1")
    path2 = r'D:\pic\jilin2023\schoolList0922.xlsx'  # 匹配校名表
    df2 = pd.read_excel(path2, sheet_name='Sheet1')
    path3 = r'D:\pic\jilin2023\majorMatch0918.xlsx'  # 匹配专业表
    df3 = pd.read_excel(path3, sheet_name='Sheet1')

    sch_inf, major_inf = school_major_deal(df2, df3)

    result, name = judge_cut(df1, sch_inf, major_inf)

    df4 = pd.DataFrame(result, columns=name)

    path4 = r'C:\Users\John\Desktop\{}（匹配）.xlsx'.format(k)  # 结果保存位置
    df4.to_excel(path4, index=False)
