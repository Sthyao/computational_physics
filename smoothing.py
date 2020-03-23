import numpy as np
import matplotlib.pyplot as plt

def main(N):
    array = np.random.rand(N,1000)
    xArray = array.mean(axis=0)
    std = xArray.std()
    return std
    #return xArray

def linerfive(array):
    number = len(array)
    out = np.zeros(number)
    if number < 5:
        return array
    else:
        out[0] = (3.0*array[0] + 2.0*array[1] + array[2] - array[4]) / 5.0
        out[1] = (4.0*array[0] + 3.0*array[1] + 2.0*array[2] + array[3]) / 10.0
        for i in range(2,number-2):
            out[i] = (array[i-2] + 3.0*array[i-1] + array[i] + array[i+1] + array[i+2]) / 5.0
        out[number-2] = (4.0*array[number-1] + 3.0*array[number-2] + 2.0*array[number-3] + array[number-4]) / 10.0
        out[number-1] = (3.0*array[number-1] + 2.0*array[number-2] + array[number-3] - array[number-5]) / 5.0
        return out

def cubicfive(array):
    N = len(array)
    out = np.zeros(N)
    if N < 5:
        return array
    else:
        out[0] = (69.0*array[0] + 4.0*array[1] - 6.0*array[2] + 4.0*array[3] - array[4]) / 70.0
        out[1] = (2.0 * array[0] + 27.0 * array[1] + 12.0 * array[2] - 8.0 * array[3] + 2.0 * array[4]) / 35.0
        for i in range(2,N-2):
            out[i] = (-3.0*array[i-2] + 2*array[i+2] + 12.0*array[i-1] + 12.0*array[1+i] + 17.0*array[i]) / 35.0
        out[N-2] = (2.0*array[N-5] - 8.0*array[N-4] + 12.0*array[N-3] + 27.0*array[N-2] + 2.0*array[N-1]) / 35.0
        out[N-1] = (-array[N-5] + 4.0*array[N-4] - 6.0*array[N-3] + 4.0*array[N-2] + 69.0 * array[N-1]) / 70.0
    return out

xt = np.arange(50)
yt0 = np.zeros(50)
for i in range(50):
    yt0[i] = main(i+1)
yt15 = linerfive(yt0)
yt35 = cubicfive(yt0)

plt.plot(xt,yt0)
plt.plot(xt,yt15)
plt.plot(xt,yt35)
plt.title("Smooth Processing Of 5 points")
plt.legend(['Source','Linear','Club'],loc = 'upper right')
plt.show()