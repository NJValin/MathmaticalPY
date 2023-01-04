__package__
import math
class DualNum:
    
    def __init__(self, a:float, b:float)-> None:
        self._a_ = a
        self._b_ = b
    
    def __add__(self, other):
        if (other is DualNum or int or float)==False:
            raise ValueError("Other must be a DualNum")
        if (other is (float or int)):
            return DualNum(self._a_+other, self._b_)
        a = DualNum(self._a_+other._a_, self._b_+other._b_)
        return a
    
    def __sub__(self, other):
        if (other is int or float): 
            return DualNum(self._a_-other, self._b)
        if (other is DualNum)==False:
            raise ValueError("Other must either be a number or a dual number")
        return self+((-1)*other)

    def __mul__(self, other):
        if (other is DualNum or int or float)==False:
            raise ValueError("Other must be a DualNum or int or float")
        if other is (int or float):
            return DualNum(self._a_*other, self._b_*other)
        a = self._a_*other._a_
        b = self._a_*other._b_+self._b_*other._a_
        return DualNum(a, b)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if (other is DualNum or int or float)==False:
            raise ValueError("Other must be a DualNum or int or float")
        if other is int or float==True:
            return DualNum(self._a_/other, self._b_/other)
        a = self._a_/other._a_
        b = (self._b_*other._a_-self._a_*other._b_)/(other._a_*other._a_)
        return DualNum(a,b)

    def __floordiv__(self, other):
        if (other is DualNum or int or float)==False:
            raise ValueError("Other must be a DualNum")
        if other is (int or float):
            return DualNum(self._a_//other, self._b_//other)
        a = self._a_//other._a_
        b = math.floor(((self._b_*other._a_)-(self._a_*other._b_))/(other._a_*other._a_))
        return DualNum(a,b)

    def __pow__(self, other):
        if other is int == False:
            raise ValueError("The power must be an integer")
        for i in range(0, other):
            x = self*self
        return x

    def Re(self):
        return self._a_
    
    def dualPart(self):
        return self._b_

    
    def __str__(self):
        return "{0}+{1}ε".format(self._a_, self._b_)

