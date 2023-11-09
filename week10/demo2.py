import numpy as np
import matplotlib.pyplot as plt

### 引入库函数
import numpy as np 
from scipy import interpolate as inter
import matplotlib.pyplot as plt
from scipy import constants as Const

# 单位(1E=30.24cm)
E = 30.24
d = 57 * E #直径
S = np.pi *(1/4)*d**2   #底面积

time = np.array([0,3316,3353,10619,13937,17921,21240,25223,28543,
				 32284,39435,43318,44363,49953,53936,57254,60574,
				 64554,68535,71854,75021,85968,89953,93270])
veetase = np.array([3175,3110,3054,2994,2947,2892,2850,2795,2795,
					2697,3550,3445,3350,3260,3167,3087,3012,2927,
					2842,2767,2697,3475,3397,3340])

f = inter.interp1d(time,veetase,kind ="quadratic",fill_value="extrapolate") #进行二次样条插值
xli = np.linspace(0,93270,200)
yli = f(xli)

plt.scatter(time,veetase,color = 'b')
plt.plot(xli,yli,'-',color = 'r') 
plt.legend(['data','quadratic'], loc='best') 
plt.xlabel('Time(s)')
plt.ylabel('veetase(cm)')
plt.show()

# 求导
def get_derivative(f, delta=0.001):
	def derivative(x):
		return (f(x+delta)-f(x))/delta
	return derivative

fd = get_derivative(f)
Flow_Rate = fd(yli * S)

plt.plot(xli,Flow_Rate,'-',color = 'b') 
plt.legend(['predict'], loc='best') 
plt.xlabel('Time(s)')
plt.ylabel('Flow Rate (cm^2)')
plt.show()
