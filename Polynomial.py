__package__
from DualNum import *
from Functions import convolve
import numpy as np
class Polynomial:
    
    def __init__(self, *coefficients):
        if isinstance(coefficients[0], list):
            self.coefficients = coefficients[0]
        else:
            self.coefficients  = [i for i in coefficients]
        self.__len__  = len(self.coefficients)
    
    def __str__(self) -> str:
        s = ""
        x = len(self.coefficients)-1
        self.coefficients.reverse()
        while x >=0:
            if x==1:
                if self.coefficients[x]!=1 or self.coefficients[x]!=0:
                    s += "{0}x+".format(self.coefficients[x], x)
                    x-=1
                elif self.coefficients[x]==1:
                    s += "x".format(self.coefficients[x], x)
                    x-=1
                else:
                    x-=1
            elif x==0:
                if self.coefficients[x]!=0:
                    s += "{0}".format(self.coefficients[x], x)
                    x-=1
                else:
                    x-=1
            else:
                if self.coefficients[x]!=1 or self.coefficients[x]!=0:
                    s += "{0}x**{1}+".format(self.coefficients[x], x)
                    x-=1
                elif self.coefficients[x]==1:
                    s += "x**{1}+".format(self.coefficients[x], x)
                    x-=1
                else:
                    x-=1
        return s
    
    def eval(self, x):
        if type(x)==float or type(x)==int or type(x)==complex or type(x)==DualNum:
            value = 0
            index = self.__len__-1
            while index>=0:
                value = value+self.coefficients[index]*x**(index-1)
                index -= 1
            return value
        return 0
    
    def multiply(self, other):
        newCoefficients = convolve(self.coefficients, other.coefficients)
        return Polynomial(newCoefficients)
    
    

