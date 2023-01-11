__package__
from DualNum import *

class Matrix:
    def __init__(self,m:int, n:int):
        self.__m = m
        self.__n = n
        self.matrix = [[0 for x in range(n)] for y in range(m)] 
    
    def set(self, i:int, j:int, value)->None:
        self.matrix[i][j]=value
    
    def get(self, i:int, j:int)->object:
        return self.matrix[i][j]
    
    def transpose(self):
        '''
        
        Returns
        -------

        Example
        -------
        >>> print(x)
        | 2 3 4 |
        | 2 3 4 |
        >>> print(x.transpose())
        | 2 2 |
        | 3 3 |
        | 4 4 |
        
        '''
        x = Matrix(self.__n, self.__m)
        
        for col in range(self.__n):
            for row in range(self.__m):
                x.set(col, row, self.matrix[row][col])
        return x
    
    def __str__(self) -> str:
        x = 0
        for row in self.matrix:
            for col in row:
                if len(col.__str__())>x:
                    x = len(col.__str__())
        string2 = ""
        for row in self.matrix:
            string2 += "|"
            for col in row:
                string2 += " {0:^{1}}".format(col, x)
            string2+=f" |\n"
        return string2

if __name__ == '__main__':
    x = Matrix(3, 4)
    print(x)
    y = DualNum(2,3)
    x.set(2, 2, y)
    print(x)
