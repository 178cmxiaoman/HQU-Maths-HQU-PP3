import os
import pandas as pd

# 找出近五年平均净利润率最高的股票
source_path = 'week13/data/transformed/'

MAX = -1000
for filename in os.listdir(source_path):
    if filename.endswith('.xls'):
        # 构建完整的文件路径
        file_path = os.path.join(source_path, filename)
        # 读取Excel文件
        df = pd.read_excel(file_path)
        df = df[['科目\时间','销售净利率']]
        df = pd.DataFrame(df)
        # 筛选近五年记录
        df['科目\时间'] = pd.to_datetime(df['科目\时间'])
        df = df[df['科目\时间'] >= pd.to_datetime('2018-01-01')]
        # 删除--记录
        df = df[df['销售净利率'] != '--']
        # 字符串转换为numeric数据类型
        df['销售净利率'] =  df['销售净利率'].str.rstrip('%').astype('float') / 100
        # 求平均值
        Mean = df['销售净利率'].mean()
        print(filename,'销售净利率为：',Mean)
        if Mean > MAX :
            MAX = Mean
            Excel = filename
print('--------------------------------')
print('for ended')
print('近五年平均净利润最高的股票为：',filename,',其平均净利润率为：',MAX,'%')
