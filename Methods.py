__package__
import math
import random
import numpy as np
from Functions import *

def isPrime(p:int, *args:int):
    """
    # Parameters
    """
    k = 30
    if p%2==0 :
        return False
    if p==1 or p==2 or p==3 or p==5  or p==7:
        return True
    pn1= p-1
    
    s = math.floor(log(pn1, 2))
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

print(isPrime(1163))


