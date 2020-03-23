import math
import numpy as np

def f(x):
    std = 15.0
    mean = 50.0
    return math.exp((-(x-mean)/(std))**2/2) / (std*math.sqrt(2*np.pi))

def quadratic()