# 
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,a):
        return point(self.x + a.x, self.y + a.y)
    def __str__(self):
        return f"{self.x}, {self.y}"
    
p1 = point(4,5)
p2 = point(6,7)
print(p1+p2)