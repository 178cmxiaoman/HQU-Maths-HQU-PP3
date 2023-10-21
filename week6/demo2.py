import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)
y = x ** 2
z = x ** 3
plt.xlabel("x label")
plt.ylabel("y label")
plt.plot(x, x)
plt.plot(x, y)
plt.plot(x, z)
plt.title('Simple Plot')
plt.legend(['linear', 'quadratic', 'cubic'])
plt.show()
