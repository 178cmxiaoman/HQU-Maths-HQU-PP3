import numpy as np

# 创建从0到19的一维数组arr
arr = np.arange(20)
print('创建从0到19的一维数组arr:')
print(arr)

# （1）将arr中的所有奇数替换为-1
s = slice(1, 20, 2)  # 从索引 1 开始到索引 20 停止，间隔为2
arr[s] = -1
print('（1）将arr中的所有奇数替换为-1:')
print(arr)

# （2）将arr转换为4行的二维数组
arr = arr.reshape(4, 5)
print('（2）将arr转换为4行的二维数组:')
print(arr)

# （3）在数组arr中交换列1和2；
arr[:, [0, 1]] = arr[:, [1, 0]]
print('（（3）在数组arr中交换列1和2:')
print(arr)

# （4）使用索引的方式获取第二行第一列和第三行第二列的数据
print('（4）使用索引的方式获取第二行第一列和第三行第二列的数据:')
print('第二行第一列:', arr[1, 0])
print('第三行第二列:', arr[2, 1])

# （5）使用切片的方式获取7题中数组的1,2行和第2,3列的数据
print('（5）使用切片的方式获取7题中数组的1,2行和第2,3列的数据:')
s1 = slice(0, 2, 1)
s2 = slice(1, 3, 1)
print(arr[s1, s2])

# （6）使用切片与整数混合使用的方法，获取数组中第二行第2,、3列数据
print('（6）使用切片与整数混合使用的方法，获取数组中第二行第2,、3列数据:')
s3 = slice(1, 3, 1)
print(arr[1, s2])

# （7）使用花式索引获取数组中索引为（2,2）和（1,3）的元素
print('（7）使用花式索引获取数组中索引为（2,2）和（1,3）的元素:')
print(arr[[2, 1], [2, 3]])

#############################
print('##################################')
# 2.已知数据集iris.data（参考百度文库），完成下列操作：
# （1）使用genfromtxt函数导入鸢尾植物数据集
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf-8')

# （2）从问题（1）中导入的一维鸢尾植物数据集中提取文本列的物种
print('（2）从问题（1）中导入的一维鸢尾植物数据集中提取文本列的物种:')
species = np.array([row[4] for row in iris])
print(np.unique(species))

# （3）求出鸢尾植物萼片长度的平均值、中位数和标准差（第1列）
print('（3）求出鸢尾植物萼片长度的平均值、中位数和标准差（第1列）:')
length = np.array([row[0] for row in iris])
print('鸢尾植物萼片长度的平均值为：', np.mean(length))
print('鸢尾植物萼片长度的中位数为：', np.median(length))
print('鸢尾植物萼片长度的标准差为：', np.std(length))

# （4）创建一种标准化形式的鸢尾植物间隔长度，其值正好介于0和1之间，这样最小值为0，最大值为1
print('（4）创建一种标准化形式的鸢尾植物间隔长度，其值正好介于0和1之间，这样最小值为0，最大值为1:')

width = np.array([row[1] for row in iris])
WIDTH_MAX = np.max(width)
WIDTH_MIN = np.min(width)
i = 0
for w in width:
    width[i] = (w - WIDTH_MIN) / (WIDTH_MAX - WIDTH_MIN)
    i = i + 1
print(width)

# （5）在数据集中的20个随机位置插入np.nan值
print('（5）在数据集中的20个随机位置插入np.nan值:')
INDEXI_i = np.random.randint(0, 150, size=20)
INDEXI_j = np.random.randint(0, 5, size=20)
for i in range(20):
    iris[INDEXI_i[i]][INDEXI_j[i]] = np.nan
print(iris)

# （6）在完成问题（5）的基础上的sepallength中查找缺失值的数量和位置
print('（6）在完成问题（5）的基础上的sepallength中查找缺失值的数量和位置:')
count = 0
for i in range(150):
    for j in range(4):
        if np.isnan(iris[i][j]):
            print('第', i, '行，第', j + 1, '列为null值')
            count = count + 1
    if iris[i][4] == 'nan':
        print('第', i, '行，第5列为null值')
        count = count + 1
print('共有', count, '个null值')

# （7）选择没有任何nan值的行
print('（7）选择没有任何nan值的行:')
for i in range(150):
    for j in range(4):
        if np.isnan(iris[i][j]):
            continue
    if iris[i][4] == 'nan':
        continue
    print('第', i + 1, '行没有任何nan值')

# （8）在数据集中将所有出现的nan替换为0
print('（8）在数据集中将所有出现的nan替换为0:')
for i in range(150):
    for j in range(4):
        if np.isnan(iris[i][j]):
            iris[i][j] = 0
    if iris[i][4] == 'nan':
        iris[i][4] = 0
print(iris)