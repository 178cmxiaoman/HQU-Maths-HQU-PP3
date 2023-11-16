# 1载入数据及数据观察,使用info,describe函数
import numpy as np
import pandas as pd

# 载入数据
file_path = './week11/bank-additional-full.csv'
df = pd.read_csv(file_path, delimiter=';')  
df.info()
print('------------------')
print(df.describe())
print('共有：',df.shape[0],'行')
print('------------------------------------------')

###########################################################
# 2.1直接删除job和matrial中unknow记录
df1 = df[(df['job'] != 'unknown') & (df['marital'] != 'unknown')]
del_num = df.shape[0] - df1.shape[0]
print('删除后还有：',df1.shape[0],'行,共删除了',del_num,'行')
print('------------------------------------------')

###########################################################
# 2.2变量education,default,housing和loan缺失数过多，不宜直接删除，采用预测方法拟合缺省值。
from sklearn.preprocessing import LabelEncoder

df2 = df1.copy()

# 要填充的列列表
temp_columns = ['education', 'default', 'housing', 'loan']

# 先用一个特殊值填充缺失值
for col in temp_columns:
    df2[col].fillna('Missing', inplace=True)

# 使用标签编码将非数字列转换为数字
label_encoders = {}
for col in temp_columns:
    label_encoders[col] = LabelEncoder()
    df2[col] = label_encoders[col].fit_transform(df2[col])

# 显示填充后的数据框架的前几行
print(df2.head())
print('------------------------------------------')

###########################################################
# 2.3.分类变量数值化处理
df3 = df2.copy()

# 识别所有分类列（pandas中的object类型列）
temp_columns = df3.select_dtypes(include=['object']).columns

# 对每个分类列应用标签编码
for col in temp_columns:
    df3[col] = df3[col].astype('category').cat.codes

# 显示前几行
print(df3.head())
print('------------------------------------------')


###########################################################
# 2.4.数据规范化
from sklearn.preprocessing import MinMaxScaler
df4 = df3.copy()
scaler = MinMaxScaler() # 初始化 MinMaxScaler
# 进行归一化
df4 = pd.DataFrame(scaler.fit_transform(df4), columns=df4.columns)

# 显示前几行
print(df4.head())
print('------------------------------------------')


###########################################################
# 3.模型的训练与评估
# 3.1数据重采样
from sklearn.utils import resample
import pandas as pd

class_counts_before = df['y'].value_counts()
df_majority = df[df['y'] == 'no']
df_minority = df[df['y'] == 'yes']

# 对多数类别进行下采样
df_majority_downsampled = resample(df_majority,
                                   replace=False,
                                   n_samples=len(df_minority),  
                                   random_state=123) 

# 将少数类别与下采样后的多数类别合并
df_resampled = pd.concat([df_majority_downsampled, df_minority])
class_counts_after = df_resampled['y'].value_counts()

print("采样前各种类别数量:\n", class_counts_before)
print('\n')
print("采样后各种类别数量:\n", class_counts_after)
print('------------------------------------------')


###########################################################
# 3.2划分数据集
from sklearn.model_selection import train_test_split

# 划分重采样后的数据集为训练集和测试集 (70% 训练集, 30% 测试集)
X = df_resampled.drop('y', axis=1)
Y = df_resampled['y']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

print("训练集大小:", X_train.shape[0])
print("测试集大小:", X_test.shape[0])
print('------------------------------------------')



###########################################################
# 3.3使用逻辑回归、随机森林、支持向量机进行分类
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.utils import resample
import pandas as pd

# 将所有分类变量转换为数值类型
df_numeric = df.copy()
categorical_columns = df_numeric.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df_numeric[col] = df_numeric[col].astype('category').cat.codes

# 重采样
df_majority = df_numeric[df_numeric['y'] == 0]
df_minority = df_numeric[df_numeric['y'] == 1]
df_majority_downsampled = resample(df_majority, 
                                   replace=False,    
                                   n_samples=len(df_minority),  
                                   random_state=123)
df_resampled = pd.concat([df_majority_downsampled, df_minority])

# 划分数据集
X = df_resampled.drop('y', axis=1)
y = df_resampled['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 应用逻辑回归、随机森林和支持向量机模型
logreg = LogisticRegression()
rf = RandomForestClassifier()
svc = SVC()

logreg.fit(X_train, y_train)
rf.fit(X_train, y_train)
svc.fit(X_train, y_train)

y_pred_logreg = logreg.predict(X_test)
y_pred_rf = rf.predict(X_test)
y_pred_svc = svc.predict(X_test)

# 分类报告
report_logreg = classification_report(y_test, y_pred_logreg)
report_rf = classification_report(y_test, y_pred_rf)
report_svc = classification_report(y_test, y_pred_svc)

print("逻辑回归:\n", report_logreg)
print("随机森林:\n", report_rf)
print("支持向量机:\n", report_svc)
