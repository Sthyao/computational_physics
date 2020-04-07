#wave equation 
#schrodinger equation and difference

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

ah = 0.5
h = 0.1
T = 0.5


def f(x):
    return math.sin(np.pi * x)

def fdt(x):
    return x*(1-x)

def main(dt):
    N = int(1.0/h)
    M = int(T/dt)  
    y = np.zeros((M,N))
    for j in range(N):
        y[0][j] = f(h*j)
    for j in range(2,N-1):
        y[1][j] = (1-ah**2)*f(j*h) + ah**2 / 2 *(f((j-1)*h) + f((j+1)*h))*dt*fdt(j)
    for i in range(2,M):
        for j in range(1,N-1):
            y[i][j] = 2 * (1 - ah**2) * y[i-1][j] + ah**2 * (y[i-1][j-1] + y[i-1][j+1]) - y[i-2][j]
    
    return(y)
        
            


dt = 0.001
y = main(dt)

xar = np.arange(10)*0.1
yar = np.arange(int(T/dt))*0.001

X, Y = np.meshgrid(xar, yar)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(Y,X,y,cmap='rainbow')
ax.set_xlabel('t')
ax.set_ylabel('x')
plt.show()