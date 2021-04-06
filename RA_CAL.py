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
io = r"C:\Users\Administrator\Desktop\python\TCZ受试者资料 20210126.xlsx"
data =pd.read_excel(io, sheet_name = "丽珠", header = None)

# data.drop(index=[0,1], inplace=True)
# data.reset_index(drop = True, inplace=True)
data.drop(data.columns[0:2], axis=1,inplace = True)
data.drop(data.index[:1], inplace = True)

# 对病人原始情况数据进行处理
data_history = data.loc[:,1:28]
data_history.columns = list(data_history.iloc[0])
data_history.drop(data_history.index[:1], inplace = True)

# 对病人基线期数据进行处理，即V0期
data_v0 = data.loc[:,30:71]
data_v0.columns = list(data_v0.iloc[0])
data_v0.drop(data_v0.index[:1], inplace = True)
# data_v0.insert(1,data_history.columns['姓名'])
# data_v0['姓名'] = data_history.columns['姓名']

# 对病人V4期数据进行处理，即第四周
data_v4 = data.loc[:, 72:113]
data_v4.columns = list(data_v4.iloc[0])
data_v4.drop(data_v4.index[:1], inplace = True)

# 对病人V6期数据进行处理，即第六周
data_v6 = data.loc[:, 114:155]
data_v6.columns = list(data_v6.iloc[0])
data_v6.drop(data_v6.index[:1], inplace = True)

# 对病人V9期数据进行处理，即第九周
data_v9 = data.loc[:, 156:197]
data_v9.columns = list(data_v9.iloc[0])
data_v9.drop(data_v9.index[:1], inplace = True)

# 输入各个表格数据
data_history.to_csv(r"C:\Users\Administrator\Desktop\python\data_history.csv")
data_v0.to_csv(r"C:\Users\Administrator\Desktop\python\data_v1.csv")
data_v4.to_csv(r"C:\Users\Administrator\Desktop\python\data_v4.csv")
data_v6.to_csv(r"C:\Users\Administrator\Desktop\python\data_v6.csv")
data_v9.to_csv(r"C:\Users\Administrator\Desktop\python\data_v9.csv")
# AAA = ['aaa',55,'M','N','N','Y','N','N','Y','N','Y']
# data.to_csv(r"C:\Users\Administrator\Desktop\python\aaa.csv")
# aa = ERS_RA.ERS_RA_Persion('aaa',55,'M','N','N','Y','N','N','Y','N','Y')
# aa.name, aa.age, aa.gender, aa.diabets, aa.hyperlinder, aa.hypertension, aa.tobacoo, aa.CDAI, aa.MHAQ, aa.
