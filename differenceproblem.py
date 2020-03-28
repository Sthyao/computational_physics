#Heat conduction and decomposition

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = np.zeros((11,37))
h = 0.1
a = 1./6
for i in range(10):
    u[i][0] = 4*i*h*(1-i*h)
for i in range(36):
    for k in range(10):
        u[k][i+1] = a * u[k+1][i] + (1-2*a)* u[k][i] + a*u[k-1][i]

ux = np.zeros((37,37))
for i in range(37):
    if i >= 0 and i<= 10:
        for j in range(37):
            ux[i][j] = u[i][j]
#print(u)

x = np.arange(37)*0.1
y = np.arange(37)*0.001/6
X, Y = np.meshgrid(y, x)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,ux,cmap='rainbow')
ax.set_xlabel('t')
ax.set_ylabel('x')
plt.show()
