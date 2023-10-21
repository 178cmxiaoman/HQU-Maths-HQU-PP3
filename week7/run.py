# 1.导入pandas库并简写为pd，并输出版本号
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

print('pandas版本号为：', pd.__version__)

# 2.从列表创建Seris
data = [1, 2, 3, 4, 5]
Series = pd.Series(data)
print('从列表创建Seris')
print(Series)

# 3.使用read_csv打开ex_data4.csv文件，变量命名为df
df = pd.read_csv('week7/data/ex_data4.CSV', encoding='gbk')

# 4.显示df的前3行
print('显示df的前3行:')
print(df.head(3))

# 5.取出索引为[1,2,5]行的animal和age列
print('取出索引为[1,2,5]行的animal和age列:')
rows = df.loc[[1, 2, 5], ['animal', 'age']]
print(rows)

# 6.取出age值缺失的行
print('取出age值缺失的行:')
missing_rows = df[df['age'].isnull()]
print(missing_rows)


# 7.取出age值在2，4间的行
print('取出age值在2，4间的行:')
age = df[(df['age'] >= 2) & (df['age'] <= 4)]
print(age)


# 8.计算每个不同种类animal的age的平均数
print('计算每个不同种类animal的age的平均数:')
average = df.groupby('animal')['age'].mean()
print(average)

# 9.使用字典创建如下信息所示的dataframe,并保存至data.csv，使用groupby分别计算Male和Female的分数Score的均值。
data = {
    'Name': ['Alen', 'Bob', 'Cidy', 'Daniel', 'Ellen', 'Frankie', 'Gate', 'Hebe'],
    'Gender': ['Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female'],
    'Age': [18, 19, 18, 20, 17, 21, 20, 22],
    'Score': [80, 90, 93, 87, 96, 100, 88, 98],
}
df = pd.DataFrame(data)
df.to_csv('week7/out/data.csv', index=False)

mean_scores = df.groupby('Gender')['Score'].mean()
print(mean_scores)


# 10. 使用read_csv打开000566.csv文件，要求：
# （1）	计算每月份平均换手率，并保存在文件result.csv。
df = pd.read_csv('week7/data/000566.csv', encoding='gbk')
data = pd.DataFrame(df)
data['日期'] = pd.to_datetime(data['日期'])  # 将时间作为索引
data = data.set_index('日期')
df1 = data.resample('m', closed='left')['换手率'].mean()
df1 = pd.DataFrame(df1)
df1.to_csv('week7/out/result.csv')


# （2）	绘制5月-8月期间的周k线图。（上网查阅股票周k线图概念）
# 方法一
df = pd.read_csv('week7/data/000566.csv', encoding='gbk')
may_to_aug_data = df[(df['日期'] >= '2021-05-01') & (df['日期'] <= '2021-08-31')]
plt.figure(figsize=(12, 6))
plt.plot(may_to_aug_data['日期'], may_to_aug_data['收盘价'], label='收盘价', marker='o')
plt.plot(may_to_aug_data['日期'], may_to_aug_data['最高价'], label='最高价', linestyle='--')
plt.plot(may_to_aug_data['日期'], may_to_aug_data['最低价'], label='最低价', linestyle='--')
plt.plot(may_to_aug_data['日期'], may_to_aug_data['开盘价'], label='开盘价', linestyle='--')
plt.title('周K线图 (5月-8月)')
plt.xlabel('日期')
plt.ylabel('价格')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 方法二
df = pd.read_csv("week7/data/000566.csv", encoding='gbk')
may_to_aug_data = df[(df['日期'] >= '2021-05-01') & (df['日期'] <= '2021-08-31')]
may_to_aug_data = may_to_aug_data.rename(columns={'开盘价': 'Open', '最高价': 'High', '最低价': 'Low', '收盘价': 'Close', '成交量': 'Volume'})
may_to_aug_data['日期'] = pd.to_datetime(may_to_aug_data['日期'])
may_to_aug_data.set_index('日期', inplace=True)
mpf.plot(may_to_aug_data, type='candle', title='Weekly K-chart for May-August', ylabel='价格',
         style='yahoo', volume=True, figratio=(12, 6), tight_layout=True)


