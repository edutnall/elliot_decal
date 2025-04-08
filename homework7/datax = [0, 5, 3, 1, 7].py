datax = [0, 5, 3, 1, 7]
datay = [3, 53, 33, 14, 73]
def error(x, y):
    def f(x):
        return 10*x+3
    final = 0
    for i in range(len(x)):
        final += (f(x[i])-y[i])**2
    error = final/len(x)
    return error
error(datax, datay)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as fit

df = pd.read_csv("S25_cf_demo_data.csv")
df.head()

plt.figure()
plt.scatter(df["x"], df["y"])
plt.show()

def f(x, m, b):
    return m*x+b

p0 = [1,1]

params, cov = fit.curve_fit(f, df["x"], df["y"], p0)

m = params[0]
b = params[1]

y_est = m*df["x"] +b

plt.figure()
plt.plot(df["x"], y_est)
plt.scatter(df["x"],df["y"])
plt.show()

residuals = y_est - df["y"]
plt.figure()
plt.scatter(y_est, residuals)
plt.show()