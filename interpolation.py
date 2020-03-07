#Lagrange
import numpy as np 
import matplotlib.pyplot as plt 
import math

N1 = 2
N2 = 4
N3 = 6

def normel(array):
    mean = 50
    std = 15
    return np.exp(-(array-mean)**2 / (2*std**2)) / (math.sqrt(2*math.pi) * std)

def lagrange(n,xarray,yarray):
    narray = np.linspace(5,95,n)
    l = np.zeros(n)
    for i in range(len(xarray)):
        temp = np.zeros(n)
        temp = temp+yarray[i]
        for j in range(len(xarray)):
            if j == i:
                continue
            else:
                temp = temp*(narray - xarray[j]) / (xarray[i] - xarray[j])
        l = l+temp
    return l

x1 = np.linspace(5,95,N1+1)
y1 = normel(x1)
x2 = np.linspace(5,95,N2+1)
y2 = normel(x2)
x3 = np.linspace(5,95,N3+1)
y3 = normel(x3)

n=40
init = np.linspace(5,95,n)
l1 = lagrange(n,x1,y1)
l2 = lagrange(n,x2,y2)
l3 = lagrange(n,x3,y3)

plt.plot(init,l1,c = 'c')
plt.plot(init,l2,c = 'c')
plt.plot(init,l3,c = 'c')
plt.plot(init,normel(init),c = 'r')
plt.title("Lagrange polynomial")
plt.show()


