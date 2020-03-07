import numpy as np 
import matplotlib.pyplot as plt 
#import seaborn as sns

def main(N):
    array = np.random.rand(N,1000)
    xArray = array.mean(axis=0)
    std = xArray.std()
    return std
    #return xArray

def delete(array):
    std = array.std()
    mean = array.mean()
    array[abs(array-mean) > 3*std] = 2
    num = 0
    for i in range(len(array)):
        if array[i] == 2:
            print("we got one")
            num = num + 1
    print("All",num)
    return array

def frequency(array,num=0):
    fArray = np.zeros(10)
    for i in range(10):
        tempArray = array[array>= 0+i*0.1 ]
        tempArray = tempArray[tempArray <= 0.1+i*0.1]
        fArray[i] = len(tempArray)
    fArray = fArray/(1000-num)
    return fArray

#part1
xArray = main(3)

plt.plot(range(1000),xArray,linewidth=0.5)
plt.title("1000 Times Of Simple Random Numbers' Average(N = 10)")
plt.show()

#part2
xArray = main(3)
xArray = delete(xArray)
fArray = frequency(xArray,13)

plt.bar(np.arange(10)/10,fArray,width=0.05)
plt.title("New Frequency When N = 10")
plt.show()

#part 3
stdArray = np.zeros(50)
for i in range(50):
    stdArray[i] = main(i)

plt.plot(range(1,51),stdArray)
plt.title("Change Of N From 1 to 50 And Its Standard Deviation")
plt.show()

#part 4

#print("The average of x is" , mean)
#print("The Std of x is" , std)

