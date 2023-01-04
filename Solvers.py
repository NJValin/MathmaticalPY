__package__
import math

@staticmethod
def nwtMth(f, x):
    h = 0.00001
    func = lambda x: eval(f)
    df = lambda x: (func(x+h)-func(x-h))/(2*h)
    for i in range(200):
        xn = x - (func(x)/df(x))
        x = xn
    return x
