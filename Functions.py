__package__

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as i
from Methods import isPrime
from Integrals import *

global e ; e= 2.7182818284590452353602874713526624977572470936999595749 
global pi; pi=3.141592653589793238462643383279
global tau; tau = 2*pi
global goldenRatio; goldenRatio=1.618033988749894848204586834365638117720309179805762862135448622705
 
def log(input:float, base:float=2)->float:
    '''Returns the log₂(input)

    Parameters
    --------------------------------
    input : The value of log that will be returned
            must be greater than (and not equal to) 0.0
    base : Set to `2` by default; for the natural log, use
           :func:`~ln`

    '''
    if input<=0:
        raise ValueError("Input value outside of function domain")
    x_i = (input-1)/(input+1)
    base_i=(base-1)/(base+1)
    enumnumerator =0
    enumdenominator =0
    for i in range(0, 2500):
        enumnumerator += (2/(2*i+1))*x_i**(2*i+1)
    for j in range(0,2500):
        enumdenominator+=(2/(2*j+1))*base_i**(2*j+1)
    return round(enumnumerator/enumdenominator, 16)

def ln(input:float):
    return log(input, e)
 
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

def Bessel( value:float, type:int=1,):
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

def Pi(x:int)->int:
    """The prime-counting function, returns the number of prime numbers up to the input integer x.\\
       Called pi function π(x)
    
    Parameters
    ----------
    x : A natural number that is the
    """
    accumulator = 0
    for i in range(1,x+1):
        prime = isPrime(i)
        accumulator = accumulator+1 if prime else accumulator
    return accumulator

def si(x:float)->float:
    return -integrate(x, 500, sinc)

def fourier(frequency:float, functionInTime:object)->complex:
    """
    Returns the
    """
    f = lambda x: functionInTime(x)*np.exp(-complex(0, -2*pi*frequency*x))
    x = integrate(-5000, 5000, f)
    return x

print(Pi(10**5))