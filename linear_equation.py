import numpy as np 
import math

a = np.array([
    [10,-1,-2,2,4],
    [1,-10,2,-1,-14],
    [1,1,-5,2,-10],
    [1,-2,2,-1,2]
    ],dtype=np.double)
a1 = np.array([
    [10,-1,-2,2],
    [1,-10,2,-1],
    [1,1,-5,2],
    [1,-2,2,-1]
    ],dtype=np.double)
b = np.array([[4],[-14],[-10],[2]],dtype=np.double)

def operation(array, res_array,i):
    size = 4
    for j in range(i+1,size):
            temp = array[j][i] / array[i][i]
            array[j][i] = 0
            for t in range(i+1, size+1):
                array[j][t]  = array[j][t] - temp*array[i][t]
            res_array[j] = res_array[j] - temp*array[i][size] 

def gs_line(a,b):
    size = 4
    for i in range(size):
        operation(a,b,i)
    temparray = np.zeros((size,size),dtype=np.double)
    for i in range(size):
        for j in range(size):
            temparray[i][j] = a[i][j]

    res = np.zeros(size,dtype=np.double)
    res[size-1] = b[size - 1] / temparray[size-1][size-1]
    for i in range(size-2,-1,-1):
        res[i] = (b[i] - np.dot(temparray[i][i+1:], res[i+1:])) / temparray[i][i] 
    print("Answer of Gaussian Elimination:\n",res)

def sd(a,b):
    x0 = np.array([0.0,0,0,0])
    x = np.array([0.0,0,0,0])
    flag = 1
    times = 1
    while flag:
        for i in range(4):
            temp = 0 
            tempx = x0.copy()
            for j in range(4):
                if i != j:
                    temp += x0[j] * a[i][j]
            x[i] = (b[i]-temp)/a[i][i]
            x0[i] = x[i].copy()
            print("Times:",times,x)
            times = times + 1
        if max(abs(x-tempx)) < 0.00001:
            
            flag = 0
    

    

#gs_line(a,b)
np.set_printoptions(formatter={'float': '{: 0.5f}'.format})
sd(a1,b)
#gs_line(a,b)