# 画出600276股票近五年营业总收入和净利润的直方图
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('week13/data/transformed/600276_main_report.xls')
df = df[['科目\时间','净利润(元)','营业总收入(元)']]
df = pd.DataFrame(df)
df['Date'] = pd.to_datetime(df['科目\时间'])
df1 = df[df['Date'] >= pd.to_datetime('2018-01-01')]

# 绘制 营业总收入(元) 直方图
plt.figure()
plt.bar(df1['Date'],df1['营业总收入(元)'],width=30,label='Total operating income')
plt.bar(df1['Date'],df1['净利润(元)'],width=30,label='Net profit')

plt.title('Total operating income and net profit for the last five years')
plt.xlabel('Date')
plt.ylabel('Total Revenue(RMB)')
plt.xticks(rotation=45)  # 旋转x轴标签，避免重叠
plt.legend()

# 显示图表
plt.tight_layout()
plt.show()

