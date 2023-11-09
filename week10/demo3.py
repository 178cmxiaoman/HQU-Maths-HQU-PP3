from scipy.optimize import minimize
import numpy as np

def fun(xs):
    f = np.sin(xs[0]) + 0.05 * xs[0]**2 +np.sin(xs[1]) + 0.05 * xs[1]**2
    return f

xs = np.arange(2)
res = minimize(fun, xs, method='TNC')
print('最小值为',res.fun)