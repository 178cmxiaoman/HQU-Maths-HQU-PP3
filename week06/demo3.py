import numpy as np



def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
x = f(t1)
y = np.cos(2 * np.pi * t2)

import matplotlib.pyplot as plt
import numpy as np

# plot 1:

plt.subplot(2, 1, 1)
plt.plot(t1, x ,color = 'k')
plt.scatter(t1, x , color = 'b')

# plot 2:

plt.subplot(2, 1, 2)
plt.plot(t2, y, ls = '--',color = 'r')

plt.show()
