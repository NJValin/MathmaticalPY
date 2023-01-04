__package__
import math
"""

"""

def integrate(a:float, b:float, func:object):
    """
    :param
        a: int/float - The lower bound of the integral, if the bound is ±∞ define a to be 'infty'
    :param
        b: int/float The upper bound of the integral, if the bound is +∞ use :func:`~integrals.integrateToInf`
    :param
        func: The function being integrated
    :return 
        :float: the value of the integral over that range
        
    """
    n=25500
    
    if type(func)==str:
        f = lambda x:eval(func)
    else:
        f = func
    sumOfF =0
    delx = (b-a)/n
    xi = (a+(a+delx))/2
    x = a
    for i in range(n):
        sumOfF+=f(xi)*delx
        xi = (x+(x+delx))/2
        x += delx
    return round(sumOfF, 16)


if __name__ == "__main__":
    print(integrate(0, 1, '1'))
    g = lambda x: math.exp(-(x*x))
    print(integrate(-5000, 5000, g))
    print(math.sqrt(math.pi))
