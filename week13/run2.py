import os
import pandas as pd

# 找出近五年平均利润增长率最高的股票
source_path = 'week13/data/transformed/'

MAX = -1000
for filename in os.listdir(source_path):
    if filename.endswith('.xls'):
        # 构建完整的文件路径
        file_path = os.path.join(source_path, filename)
        # 读取Excel文件
        df = pd.read_excel(file_path)
        df = df[['科目\时间','净利润同比增长率']]
        df = pd.DataFrame(df)
        # 筛选近五年记录
        df['科目\时间'] = pd.to_datetime(df['科目\时间'])
        df = df[df['科目\时间'] >= pd.to_datetime('2018-01-01')]
        # 删除--记录
        df = df[df['净利润同比增长率'] != '--']
        # 字符串转换为numeric数据类型
        df['净利润同比增长率'] =  df['净利润同比增长率'].str.rstrip('%').astype('float') / 100
        # 求平均值
        Mean = df['净利润同比增长率'].mean()
        print(filename,'净利润同比增长率为：',Mean)
        if Mean > MAX :
            MAX = Mean
            Excel = filename
            
print('--------------------------------')
print('for ended')
print('近五年平均利润增长率最高的股票为：',filename,',其净利润同比增长率为：',MAX,'%')
