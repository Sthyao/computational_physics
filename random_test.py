import numpy as np 
import matplotlib.pyplot as plt 
#import seaborn as sns


#array = np.random.rand(10,1000)
#np.save('array',array)
array = np.load('array.npy')
xArray = np.zeros(1000)
for i in range(10):
    xArray = xArray+array[i]
xArray = xArray/10
mean = xArray.mean()
std = xArray.std()
#random.rand => give a sample random number in [0,1]
#np.random.randint => only integer
#xArraySingleLine = array.ravel()

xArray[abs(xArray-mean) > 3*std] = 2

fArray = np.zeros(10)
for i in range(10):
    tempArray = xArray[xArray>= 0+i*0.1 ]
    tempArray = tempArray[tempArray <= 0.1+i*0.1]
    fArray[i] = len(tempArray)
fArray = fArray/1000



plt.bar(np.arange(10)/10,fArray,width=0.05)
plt.title("New Frequency When N = 10")
#plt.show()


print(3*std+mean)  
for i in range(1000):
    if xArray[i]>3*std+mean:
        print("we got one")


#print("The average of x is" , mean)
#print("The Std of x is" , std)
"""
plt.plot(range(1000),xArray,linewidth=0.5)
plt.title("1000 Times Of Simple Random Numbers' Average(N = 10)")
plt.show()
"""
#print(array[0])