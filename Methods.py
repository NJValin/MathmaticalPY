__package__
import math
import random
import numpy as np

def isPrime(p:int, iterations:int=30):
    """
    # Parameters
    """
    k = iterations
    if p%2==0 :
        return False
    if p==1 or p==2 or p==3 or p==5  or p==7:
        return True
    pn1= p-1
    
    s = math.floor(math.log(pn1, 2))
    d = pn1/(2**s)
    while d != math.floor(d):
        s-=1
        d = pn1/2**s
    d = int(d)
    for i in range(k):
        a = random.randint(2, p-2)
        x = pow(a, d, p)
        
        for j in range(s):
            y = pow(x,2,p)
            if y==1 and x!=1 and x!=(p-1):
                return False
            x=y
        if y!=1:
            return False
    return True

def plot(x0:float, x1:float, function:object):
    """Plots the function in the domain given as [x0, x1]
    ## Not yet complete, will be completed using a tkinter GUI

    Parameters
    ----------
    x0 : the infimum of the interval given.

    x1 : The supremum of the given interval.

    function : The function to be graphed.

    Returns
    -------
    A picture of the function plotted in the given interval (NOT YET IMPLEMENTED).
    At the moment, the function just plots the image of the function.
    """
    dx = (x1-x0)/40
    xspace = [0]*40
    x = x0
    for i in range(len(xspace)):
        x+=dx
        xspace[i] = x   
    yspace = [0]*len(xspace)
    for i in range(len(yspace)):
        yspace[i]=function(xspace[i])
    return yspace

def bisection(a:float, b:float, function:object, iterations:int=50):
    """Finds zeroes of the function f(x) in the interval [a,b].

    Parameters
    ----------
    function : The function being analysed.

    a : the infimum of the interval make sure 
        that it is the opposit of the supremum b.
    
    b : The supremum of the interval in question
    Returns
    -------
    A zero in the interval [a,b]
    if there are no zeroes in the interval, returns None

    Examples
    --------
    >>> f = lambda x: sin(x)
    >>> bisection(-pi/2, pi/2, f)
    0.0
    """
    if function(a)*function(b)>=0:
        print("Both bounds have the same sign")
        return None
    a_i = a
    b_i = b
    for i in range(iterations):
        mid = (a_i+b_i)/2
        if function(mid)*function(b_i)<0:
            a_i = mid
        elif function(mid)*function(a_i)<0:
            b_i=mid
        elif function(mid)==0:
            return mid
        else:
            print("No zero found")
            return None
    return (a_i+b_i)/2


if __name__ == "__main__":
    f = lambda x: math.exp(x)-2
    print(bisection(0,6,f))
    print(math.log(2))
