#Monte Carlo and equilibrium process 

import numpy as np
import matplotlib.pyplot as plt
import random

#0 means A, 1 means B

def main(T):
    molecule = np.zeros(10000)
    nOfb = np.zeros(T)
    for i in range(T):
        num = random.randint(0,9999)
        if molecule[num]:
            molecule[num] = 0
        else:
            molecule[num] = 1
        nOfb[i] = molecule.sum()
    return nOfb


def repetition(N):
    T = 5000
    bOfnTotal  = np.zeros((N,T))
    bOfnMean = np.zeros(T)
    for i in range(N):
        bOfnTotal[i] = main(T)
    

    bOfnMean = np.mean(bOfnTotal,axis=0)
    
    return bOfnMean

N = 20

t = np.arange(5000)/10000
b = repetition(N)
reference = 10000/2 * (1 - np.exp(-2 * t/10000))
plt.plot(t,b,linewidth=1.5,c = 'y')
#plt.plot(t,reference, linewidth=1,c = 'r')
plt.title("N in B With Monte Carlo,t in MCS")
#plt.legend(['Simulation','Theory'],loc = 'upper right')
plt.show()