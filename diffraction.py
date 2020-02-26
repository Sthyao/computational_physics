import numpy as np
import matplotlib.pyplot as plt 

th = np.arange(-1/2 * np.pi, 1/2 * np.pi,0.001)

a = 4000
d = 8000
lab = 550
N = 2

def I(x):
    u = np.pi * a * np.sin(x)  / lab
    v = np.pi * d * np.sin(x) / lab
    #v[ v < 0.0001] = 0.0001
    #u[ u < 0.0001] = 0.0001
    return 5 * (np.sin(u) ** 2) / ( u ** 2 ) * (np.sin(N * v) ** 2) / (np.sin(v) ** 2)
    #return (np.sin(N * v) / np.sin(v) ) ** 2

plt.plot(th,I(th),c = 'b')
plt.title('Multiple-slit diffraction',fontproperties='SimHei',fontsize=18,color='green')
plt.show()

