#Solutions to ordinary differential equations
#RLC and R-K

import math
import numpy as np
import matplotlib.pyplot as plt

L = 4.
V = 5.
R = 2.
C = 1.

def rk(dt):
    t = int(100/dt)
    I = np.zeros(t)
    Q = np.zeros(t)
    for i in range(t-1):
        st = dt*i
        k1 = I[i]
        l1 = 1/L * (V - Q[i]/C - I[i] /R)
        k2 = I[i] + dt*l1/2
        l2 = 1/L * (V - (Q[i] + dt*k1/2)/C - (I[i] + dt*l1/2)/R)
        k3 = I[i] + dt*l2/2
        l3 = 1/L * (V - (Q[i] + dt*k2/2)/C - (I[i] + dt*l2/2)/R)
        k4 = I[i] + dt*l3/2
        l4 = 1/L * (V - (Q[i] + dt*k3/2)/C - (I[i] + dt*l3/2)/R)

        Q[i+1] = Q[i] + 1/6 * (k1 + 2*k2 + 2*k3 + k4) * dt
        I[i+1] = I[i] + 1/6 * (l1 + 2*l2 + 2*l3 + l4) * dt
    
    return Q

dt = 0.01

x = np.arange(int(100/dt)) * dt
y = rk(dt)

plt.plot(x,y)
plt.title("RLC And R-K@4")
plt.xlabel('t/s')
plt.ylabel('Q/C')
plt.show()



