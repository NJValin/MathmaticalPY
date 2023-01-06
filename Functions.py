__package__

import math
import numpy as np
import matplotlib.pyplot as plt
from Integrals import *

global e ; e= 2.7182818284590452353602874713526624977572470936999595749 
global pi; pi=3.141592653589793238462643383279
 
def log(input:float=1, *args:float)->float:
    if input<=0:
        raise ValueError("Input value outside of function domain")
    base = e
    if (len(args)==1):
        base = args[0]
    x_i = (input-1)/(input+1)
    base_i=(base-1)/(base+1)
    enumnumerator =0
    enumdenominator =0
    for i in range(0, 2500):
        enumnumerator += (2/(2*i+1))*x_i**(2*i+1)
    for j in range(0,2500):
        enumdenominator+=(2/(2*j+1))*base_i**(2*j+1)
    return round(enumnumerator/enumdenominator, 16)


 
def convolve(A:list[float], B:list[float]) -> list[float]:
    C = []
    if (len(A)<len(B)):
        A, B = B, A
    size = len(A)+len(B)-1
    for n in range(size):
        s = 0
        for i in range(0, n+1):
            if i < len(A) and (n - i) < len(B):
                s += A[i]*B[n-i]
        C.append(s)
    return C 


def exp(val, *args:float) -> float:
    if type(val)==list:
        x = [0]*len(val)
        for i in range(len(val)):
            x[i] = exp(val[i])
        return x
    factor = 1
    if len(args) ==1:
        if args[0]==2 and type(val)==int and val>=0 and val<=15:
            btwo = [32768,16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
            return btwo[val]
        factor = log(e, args[0])
    s = 0
    for n in range (0, 200):
        s += ((factor**n)*(val**n))/math.factorial(n)
    return s

def Bessel(type:int, value:float):
    """
    # Parameters
    """
    summation = 0
    for i in range(50):
        summation+=(((-1)**i)*((value/2)**(2*i+type)))/(math.factorial(i)*math.gamma(i+type+1))
    return round(summation, 15)

def sinc(x:float)->float:
    """
    The sinc function sin(x)/x. ∀kϵ𝐙/{0}:sinc(kπ)=0
    # Parameters
    x : the value of the function computed
    """
    if x == 0:
        return 1
    else:
        return math.sin(x)/x

def nsinc(x:float) ->float:
    return sinc(pi*x)

def Si(x:float)->float:
    return integrate(0, x, sinc)

def si(x:float)->float:
    return -integrate(x, 500, sinc)

print(si(-50))