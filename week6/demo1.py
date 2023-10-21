import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
plt.plot(x, x)
ax.set_title('title')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
