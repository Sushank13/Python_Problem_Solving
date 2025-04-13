# WAP to get the slope and distance of a line
class Line:
    def __init__(self,p1,p2):
        self.x1,self.y1=p1
        self.x2,self.y2=p2
    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)
    def distance(self):
        return ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5
line=Line((1,2),(3,4))
print(line.slope())
print(line.distance())