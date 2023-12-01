import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
import numpy as np
# 应该选举哪些财务指标，选用哪种合适的聚类分析方法将股票分成三种类型。
source_path = 'week13/data/transformed/'
df = pd.DataFrame()
data = pd.DataFrame()

# 选择使用的财务指标
def fun(data):
    features = ['净利润(元)', '营业总收入(元)', '净资产收益率-摊薄', '资产负债比率']
    data = data[features]
    data = data[data['净利润(元)'] != '--']
    data = data[data['营业总收入(元)'] != '--']
    data = data[data['净资产收益率-摊薄'] != '--']
    data = data[data['资产负债比率'] != '--']
    return data

# 数据预处理：转换百分比和标准化
def pre(data):
    data['净资产收益率-摊薄'] = data['净资产收益率-摊薄'].str.rstrip('%').astype('float') / 100.0
    data['资产负债比率'] = data['资产负债比率'].str.rstrip('%').astype('float') / 100.0
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    data_scaled_df = pd.DataFrame(data_scaled, columns=data.columns)  # 将NumPy数组转换回DataFrame
    return data_scaled_df

# 示例：读取和合并多个Excel文件
for filename in os.listdir(source_path):
    if filename.endswith('.xls'):
        file_path = os.path.join(source_path, filename)
        data = pd.read_excel(file_path)
        data = fun(data)
        data = pre(data)
        df = pd.concat([df, data])

# 应用K-Means聚类
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(df)
# print(clusters)
df['Cluster'] = pd.Series(clusters)

# 输出到Excel文件
output_path = './week13/out.xlsx'  # 您可以根据需要更改文件名和路径
df.to_excel(output_path, index=False)

print(f"已将聚类结果保存到 '{output_path}'")
