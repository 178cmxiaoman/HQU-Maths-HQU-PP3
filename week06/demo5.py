import numpy as np
import matplotlib.pyplot as plt

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf-8')

length1 = np.array([row[2] for row in iris[0:50]])
width1 = np.array([row[3] for row in iris[0:50]])
plt.scatter(length1, width1, marker='s', color='b')

length2 = np.array([row[2] for row in iris[50:100]])
width2 = np.array([row[3] for row in iris[50:100]])
plt.scatter(length2, width2, marker='x', color='k')

length3 = np.array([row[2] for row in iris[100:150]])
width3 = np.array([row[3] for row in iris[100:150]])
plt.scatter(length3, width3, color='r')

plt.title('Iris Data Set')
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.grid(True)
plt.legend(['setosa', 'versicolor', 'virginica'])

plt.show()
