__package__

class Polynomial:

    def __init__(self, *args):
        self.coefficents  = [i for i in args]
        self.coefficents.reverse()
    
    def __str__(self) -> str:
        s = ""
        x = len(self.coefficents)-1
        while x >=0:
            if x==1:
                if self.coefficents[x]!=1 or self.coefficents[x]!=0:
                    s += "{0}x+".format(self.coefficents[x], x)
                    x-=1
                elif self.coefficents[x]==1:
                    s += "x".format(self.coefficents[x], x)
                    x-=1
                else:
                    x-=1
            elif x==0:
                if self.coefficents[x]!=0:
                    s += "{0}".format(self.coefficents[x], x)
                    x-=1
                else:
                    x-=1
            else:
                if self.coefficents[x]!=1 or self.coefficents[x]!=0:
                    s += "{0}x**{1}+".format(self.coefficents[x], x)
                    x-=1
                elif self.coefficents[x]==1:
                    s += "x**{1}+".format(self.coefficents[x], x)
                    x-=1
                else:
                    x-=1
        return s

print(Polynomial(1,2,3,4))