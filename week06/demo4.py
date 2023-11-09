from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

font = FontProperties(fname=r"C:\windows\Fonts\MISTRAL.ttf", size=14)
x1 = [1, 3, 5, 7, 9]
y1 = [5, 4, 8, 12, 7]
x2 = [2, 4, 6, 8, 10]
y2 = [4, 6, 8, 13, 15]

plt.bar(x1, y1)
plt.bar(x2, y2, color='orange')
plt.xlabel('number')
plt.ylabel('value')
plt.title('graph')
plt.legend(['graph 1', 'graph 2'])

plt.show()
