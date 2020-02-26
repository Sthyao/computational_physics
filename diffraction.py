import numpy as np
import matplotlib.pyplot as plt 

th = np.arange(-1/2 * np.pi, 1/2 * np.pi,0.001)

a = 4000
d = 8000
lab = 550
N = 4




def I(x):
    global u,v
    u = np.pi * a * np.sin(x)  / lab
    v = np.pi * d * np.sin(x) / lab
    u = (np.sin(u) ** 2) / ( u ** 2 )
    v = (np.sin(N * v) ** 2) / (np.sin(v) ** 2)
    #v[ v < 0.0001] = 0.0001
    #u[ u < 0.0001] = 0.0001
    return  v*u 


plt.plot(th,I(th),c = 'b')
plt.plot(th,v,c = 'y')
plt.plot(th,u,c = 'c')
plt.title('Multiple-slit diffraction',fontproperties='SimHei',fontsize=18,color='green')
plt.show()

