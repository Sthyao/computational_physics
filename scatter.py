import numpy as np
import matplotlib.pyplot as plt 
import math

k = 0.75
dt = 0.05
x0 = 40
y0 = 0



def main(init):
    position = np.zeros((2,5000))
    position[0][0] = -2
    position[1][0] = -2 + init
    vx = 1.5
    vy = 0
    r0 = math.sqrt((position[0][0]-x0)**2 + (position[1][0]-y0)**2 )
    for t in range(5000):
        if t == 0:
            ax = k*(position[0][0]-x0)/(r0**3)
            ay = k*(position[1][0]-y0)/(r0**3)
        else:
            position[0][t] = position[0][t-1] + vx*dt
            position[1][t] = position[1][t-1] + vy*dt

            r = math.sqrt((position[0][t]-x0)**2 + (position[1][t]-y0)**2 )

            ax = k*(position[0][t]-x0)/(r**3)
            ay = k*(position[1][t]-y0)/(r**3)

            vx = vx + ax*dt
            vy = vy + ay*dt
    return position

for i in range(20):
    p = main(i*0.2)
    plt.plot(p[0] , p[1], c = 'c')
plt.show()

        
