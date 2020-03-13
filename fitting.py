import numpy as np 
import matplotlib.pyplot as plt 
import math

#same as file random_test

def main(N):
    array = np.random.rand(N,1000)
    xArray = array.mean(axis=0)
    std = xArray.std()
    return std
def f1(x,c0,c1):
    return c0 + c1*x
def f2(x,c0,c1):
    return np.exp(c0 + c1*x)
def f3(x,c0,c1):
    return math.exp(c0)*np.power(x,c1)

def trans(array):
    return np.log(array)
def stD(x,y,c0,c1,typeum = 0):
    if typeum == 0:
        temp = f1(x,c0,c1) - y
    elif typeum == 1:
        temp = f2(x,c0,c1) - y
    else:
        temp = f3(x,c0,c1) - y
    return temp.std()

def ols(x,y):
#   lens = len(x)
    ex = x.mean()
    sumx2 = sum(x**2)
    sumxy = sum(x*y)
    ey = y.mean()
    c1 = (sumxy - ex*ey) / (sumx2 - ex**2) 
    c0 = ey - c1 * ex
    std = stD(x,y,c0,c1)
    std2 = stD(np.exp(x),np.exp(y),c0,c1,1)
    parameters = {'c0':c0,'c1':c1,'std1':std,'std2':std2,"mean":[ex,ey]}
    #parameters = {'c0':c0,'c1':c1}
    return parameters

stdArray = np.zeros(50)
xArray = np.zeros(50)
for i in range(50):
    xArray[i] = i+1
    stdArray[i] = main(i+1)

#dicts = ols(xArray,trans(stdArray))
dicts = ols(trans(xArray),trans(stdArray))
for key,value in dicts.items():
    print('{key}:{value}'.format(key = key, value = value))
    
plt.plot(xArray,f3(np.exp(xArray),dicts.get('c0'),dicts.get('c1')))
plt.plot(xArray,stdArray,c = 'b')
plt.legend(['Fitting','Source'],loc = 'upper right')
plt.title("Fitting of Variance of normal distribution")
plt.show()

#print(stdArray)
#y = a * exp(b*x)
# ln(y)  = a + b*x


#test

#xArray = np.array([1,2,3,4,5,6,7,8,9,10])
#yArray = np.array([1,2,3,4,5,6,7,8,9,10])

#print(ols(xArray,yArray))