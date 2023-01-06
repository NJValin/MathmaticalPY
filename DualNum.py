__package__
import math
import copy
class DualNum:
    
    def __init__(self, a:float, b:float)-> None:
        self.__a__ = a
        self.__b__ = b
    
    def __add__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return DualNum(self.__a__+other, self.__b__)
        a = DualNum(self.__a__+other.__a__, self.__b__+other.__b__)
        return a
    def __radd__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return DualNum(self.__a__+other, self.__b__)
        a = DualNum(self.__a__+other.__a__, self.__b__+other.__b__)
        return a
    
    def __sub__(self, other):
        if isinstance(other,int) or isinstance(other,float): 
            return DualNum(self.__a__-other, self._b)
        if type(other)!=DualNum:
            raise ValueError("Other must either be a number or a dual number")
        return self+((-1)*other)
    def __rsub__(self, other):
        if isinstance(other,) or type(other)==float: 
            return DualNum(self.__a__-other, self._b)
        if type(other)!=DualNum:
            raise ValueError("Other must either be a number or a dual number")
        return self+((-1)*other)

    def __mul__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return DualNum(self.__a__*other, self.__b__*other)
        a = self.__a__*other.__a__
        b = self.__a__*other.__b__+self.__b__*other.__a__
        return DualNum(a, b)

    def __rmul__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            return DualNum(self.__a__*other, self.__b__*other)
        a = self.__a__*other.__a__
        b = self.__a__*other.__b__+self.__b__*other.__a__
        return DualNum(a, b)

    def __truediv__(self, other):
        if (isinstance(other, DualNum) or isinstance(other, int) or  isinstance(other, float))==False:
            raise ValueError("Other must be a DualNum or int or float")
        if other is int or float==True:
            return DualNum(self.__a__/other, self.__b__/other)
        a = self.__a__/other.__a__
        b = (self.__b__*other.__a__-self.__a__*other.__b__)/(other.__a__*other.__a__)
        return DualNum(a,b)

    def __floordiv__(self, other):
        if (isinstance(other, DualNum) or isinstance(other, int) or  isinstance(other, float))==False:
            raise ValueError("Other must be a DualNum")
        if other is (int or float):
            return DualNum(self.__a__//other, self.__b__//other)
        a = self.__a__//other.__a__
        b = math.floor(((self.__b__*other.__a__)-(self.__a__*other.__b__))/(other.__a__*other.__a__))
        return DualNum(a,b)

    def __pow__(self, other):
        if isinstance(other,int)==False:
            raise ValueError("The power must be an integer")
        x = self
        for i in range(0, other):
            x *= self
        return x

    def Re(self):
        return self.__a__
    
    def dualPart(self):
        return self.__b__

    def conjugate(self):
        return DualNum(self.__a__, (-1)*self.__b__)

    
    def __str__(self):
        
        return "{0}+{1}ε".format(self.__a__, self.__b__)

