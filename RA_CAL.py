# -*- encoding: utf-8 -*-
'''
@File    :   RA_CAL.py
@Time    :   2021/04/03 10:12:44
@Author  :   Kaiqiang Li
@Version :   V1.0
'''
# here put the import lib
import ERS_RA
import pandas as pd

# 读取数据
io = r".\data.xlsx"
data_jinyu =pd.read_excel(io, sheet_name = "金宇", header = None)
# data_jinyu.drop(index=[0,1], inplace=True)
# data_jinyu.reset_index(drop = True, inplace=True)
data_jinyu.drop(data_jinyu.columns[0:2], axis=1,inplace = True)
data_jinyu.drop(data_jinyu.index[:1], inplace = True)

# 对病人原始情况数据进行处理
data_jinyu_history = data_jinyu.loc[:,1:28]
data_jinyu_history.columns = list(data_jinyu_history.iloc[0])
data_jinyu_history.drop(data_jinyu_history.index[:1], inplace = True)

# 对病人基线期数据进行处理，即V0期
data_jinyu_v0 = data_jinyu.loc[:,30:71]
data_jinyu_v0.columns = list(data_jinyu_v0.iloc[0])
data_jinyu_v0.drop(data_jinyu_v0.index[:1], inplace = True)
# data_jinyu_v0.insert(1,data_jinyu_history.columns['姓名'])
# data_jinyu_v0['姓名'] = data_jinyu_history.columns['姓名']

# 对病人V4期数据进行处理，即第四周
data_jinyu_v4 = data_jinyu.loc[:, 72:113]
data_jinyu_v4.columns = list(data_jinyu_v4.iloc[0])
data_jinyu_v4.drop(data_jinyu_v4.index[:1], inplace = True)

# 对病人V6期数据进行处理，即第六周
data_jinyu_v6 = data_jinyu.loc[:, 114:155]
data_jinyu_v6.columns = list(data_jinyu_v6.iloc[0])
data_jinyu_v6.drop(data_jinyu_v6.index[:1], inplace = True)

# 对病人V9期数据进行处理，即第九周
data_jinyu_v9 = data_jinyu.loc[:, 156:197]
data_jinyu_v9.columns = list(data_jinyu_v9.iloc[0])
data_jinyu_v9.drop(data_jinyu_v9.index[:1], inplace = True)

# 输入各个表格数据
data_jinyu_history.to_csv(r".\data_jinyu_history.csv")
data_jinyu_v0.to_csv(r".\data_jinyu_v1.csv")
data_jinyu_v4.to_csv(r".\data_jinyu_v4.csv")
data_jinyu_v6.to_csv(r".\data_jinyu_v6.csv")
data_jinyu_v9.to_csv(r".\data_jinyu_v9.csv")

data_lizhu =pd.read_excel(io, sheet_name = "丽珠", header = None)


# AAA = ['aaa',55,'M','N','N','Y','N','N','Y','N','Y']
# data_jinyu.to_csv(r"C:\Users\Administrator\Desktop\python\aaa.csv")
# aa = ERS_RA.ERS_RA_Persion('aaa',55,'M','N','N','Y','N','N','Y','N','Y')
# aa.name, aa.age, aa.gender, aa.diabets, aa.hyperlinder, aa.hypertension, aa.tobacoo, aa.CDAI, aa.MHAQ, aa.
