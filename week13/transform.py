import os
import pandas as pd

# 设置源路径和目标路径
source_path = 'week13/data/raw/'
target_path = 'week13/data/transformed/'

# 确保目标路径存在
if not os.path.exists(target_path):
    os.makedirs(target_path)

# 遍历源路径下的所有.xls文件
for filename in os.listdir(source_path):
    if filename.endswith('.xls'):
        # 构建完整的文件路径
        file_path = os.path.join(source_path, filename)
        # 读取Excel文件
        df = pd.read_excel(file_path)
        # 转置数据
        df_transposed = df.T
        # 构建转换后文件的完整路径
        transformed_file_path = os.path.join(target_path, filename)
        # 保存转置后的文件
        df_transposed.to_excel(transformed_file_path, engine='openpyxl',header=False)
        
print("所有文件已成功转置并保存到指定目录。")





