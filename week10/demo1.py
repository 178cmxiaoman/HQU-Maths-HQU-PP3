import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# 设置随机数的种子
np.random.seed(10)

# 原函数
def fun(x):
	y = x**3 - 6*x**2 + 5*x - 3
	return y

# 3次拟合函数
def tar3(x,a,b,c,d):
	return a*x**3 +b*x**2 + c*x +d

# 4次拟合函数
def tar4(x,a,b,c,d,e):
	return a*x**4 +b*x**3 + c*x**2 +d*x +e

# 2次拟合函数
def tar2(x,a,b,c):
	return a*x**2 + b*x +c

# 原始数据
raw_xs = np.arange(-5,5,0.2)
raw_ys = fun(raw_xs)

plt.plot(raw_xs,raw_ys,color = 'b')

# 噪声数据
xs = raw_xs
ys = fun(raw_xs) + np.random.randn(50)
plt.scatter(xs,ys,color = 'r')

# 三次拟合
out3, _ = curve_fit(tar3,xs,ys)
ys3 = tar3(raw_xs,out3[0],out3[1],out3[2],out3[3])
plt.plot(xs,ys3,'-',color = 'y')

# 四次拟合
out4, _ = curve_fit(tar4,xs,ys)
ys4 = tar4(raw_xs,out4[0],out4[1],out4[2],out4[3],out4[4])
plt.plot(xs,ys4,'-',color = 'g')

# 两次拟合
out2, _ = curve_fit(tar2,xs,ys)
ys2 = tar2(raw_xs,out2[0],out2[1],out2[2])
plt.plot(xs,ys2,'-',color = 'c')

print('原系数为',[1,6,5,-3])
print('三次拟合的系数为',out3)
print('四次拟合的系数为',out4)
print('两次拟合的系数为',out2)


plt.legend(['primitive function','noise figure','3rd fit','4th fit','2nd fit'])
plt.show()

