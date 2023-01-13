import math


__package__

class Vector:
    '''A class that represents a column vector in F over a field F, .
    
    '''
    __dim__:int
    __vec__:list
    def __init__(self, *values):
        for i in values:
            if type(i)!=int or type(i)!=float or type(i)!=complex:
                raise ValueError("Can only have values of a field")
        self.__dim__ = len(values)
        self.__vec__ = [i for i in values]

    def norm(self):
        return math.sqrt(self.dotProd(self))
    
    def dotProd(self, other):
        if self.__dim__!=other.__dim__:
            return None
        value = 0
        for i in range(self.__dim__):
            value += self.__vec__[i]*other.__vec__[i]
        return value

    def crossProd(self, other):
        if self.__dim__!=other.__dim__ and self.__dim__!=3:
            return None
        else:
            x = self.__vec__[1]*other.__vec__[2]-self.__vec__[2]*other.__vec__[1]
            y = self.__vec__[2]*other.__vec__[0]-self.__vec__[0]*other.__vec__[2]
            z = self.__vec__[0]*other.__vec__[1]-self.__vec__[1]*other.__vec__[0]
            return Vector(x,y,z)
    
    def __str__(self):
        rep = ''
        largestValue =0
        for i in self.__vec__:
            if len(i.__str__())>largestValue:
                largestValue = len(i.__str__())
        for i in self.__vec__:
            rep += '| {0:^{1}} |\n'.format(i, largestValue)
        return rep
