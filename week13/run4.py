import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings

# 预测000513股票2021年9月20-24日股票价格
# 读取股票数据
file_path = 'week13/data/000513.csv'  # 替换为您的文件路径
df = pd.read_csv(file_path, encoding='GBK')
df['Date'] = pd.to_datetime(df['日期'])
df = df.sort_values(by='Date', ascending=True)

# 使用 '收盘价' 数据来训练模型
df = df['收盘价']

# 拟合ARIMA模型,这里使用(5,1,0)作为模型参数
warnings.filterwarnings("ignore")
model = ARIMA(df, order=(5,1,0))
model_fit = model.fit()

# 预测接下来5天的价格
forecast = model_fit.forecast(steps=10)
out = forecast.tolist()

# 打印预测结果
for i in [2,3,4,5,6]:
    print('2021年9月', 18 + i,'日股票价格(收盘价)为：',out[i],'元')

