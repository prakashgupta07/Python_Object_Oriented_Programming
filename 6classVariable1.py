#class variable
class Circle:
        pi=3.14
        def __init__(self,radius):
                self.radius=radius
                
        def circle_circumfrance(self):
                return 2*Circle.pi*self.radius
        
c=Circle(3 )
print(c.circle_circumfrance())
