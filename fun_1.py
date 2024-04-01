class Funct:
    def __init__(self,n):
        self.n = n
    
    def add(self,t):
        res = self.n+t
        return res


f1 = Funct(5)
print(f1.add(3))

