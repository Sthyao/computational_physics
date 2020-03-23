import math
import numpy as np

ep = 0.001
lim = 100
def f(x):
    std = 15.0
    mean = 50.0
    #return x
    return math.exp((-(x-mean)/(std))**2/2) / (std*math.sqrt(2*np.pi))


def integral():
    s = np.zeros(500)
    init = 50.0
    length = 100.0
    length0 = 200
    N = 1
    RP = f(init - length/2) + f(init + length/2)
    X =  init - init - length/2
    RC = 0
    s[0] = RP +RC
    #print(s[0])
    flag = 1
    i = 0
    while flag:
        X =  -length/2
        RC = 0
        for j in range(N):
            X = X + length
            RC = RC + f(X)

        i = i+1
        s[i] = (RP + 4*RC)*length/6

        D = 10000
        if abs(length) >= length0:
            flag = 1
        else:
            flag = 0

        if flag != 1:
            D = s[i] - s[i-1]
            if abs(s[i+1]) < 1:
                D = D/s[i]
            
        if abs(D) <= ep:
            flag = 0
        else:
            flag = 1
        
        if flag:
            s[i-1] = s[i]
            RP = RP + 2*RC
            N = 2*N
            length = length/2
        #print(i)
    return {'s':s,'N':N} 

dicts = integral()
array = dicts.get('s')
N = dicts.get('N')


for i in range(200):
    if array[i] != 0:
        print(format(array[i],'.5f'))
print("N = ", N)

       

