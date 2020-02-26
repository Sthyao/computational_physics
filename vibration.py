import matplotlib.pyplot as plt
import numpy as np
 
def f1(t):
    return 1 * np.sin(1 * np.pi * t + 0)

def f2(t):
    return 1.5 * np.sin(1.5 * np.pi * t)
 
a = np.arange(0.0,5.0,0.02)
 
plt.plot(a,f1(a),c = 'r')
plt.annotate(r'x1=$\sin({\pi})$',xy=(2.5,f1(2.5)),xytext=(30, 60),textcoords='offset points',
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),fontsize=12,color='r')

plt.plot(a,f2(a),c = 'b')
plt.annotate(r'x2=$\sin({1.5\pi})$',xy=(3,f2(3)),xytext=(30,60),textcoords='offset points',
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),fontsize=12,color='b')

plt.plot(a,f1(a)+f2(a),c = 'y')
plt.annotate('x1+x2',xy=(3.2,f1(3.2)+f2(3.2)),xytext=(30,60),textcoords='offset points',
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),fontsize=12,color='y')

plt.xlabel('t',fontproperties='Kaiti',fontsize=14,color='red')
plt.ylabel('x',fontproperties='SimHei',fontsize=18,color='red')
plt.title('Vibration synthesis',fontproperties='SimHei',fontsize=18,color='green')
plt.grid(True)
plt.axis([-1,6,-3,4]) 
plt.show()
