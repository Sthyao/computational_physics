#Fast Fourier Transform

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-512,512)*0.1
y = np.cos(x) + 0.5*np.cos(2*x)+0.8*np.cos(5*x)

def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def main(x):
    x = np.asarray(x, dtype = float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError('size of x must be power of 2')
    elif N <= 32:
        return DFT_slow(x)
    else:
        X_even = main(x[::2])
        X_odd = main(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N )
        return np.concatenate([X_even + factor[:N // 2] * X_odd,
                               X_even + factor[N // 2:] * X_odd  
        ])        

yy = main(y)
plt.plot(x,y)
plt.plot(x,yy)
plt.plot(x, np.fft.fft(y))

plt.title('FFT')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Source ','FFT','FFT_self'],loc = 'upper right')
plt.show()