class shape:
    def area(self):
        pass
class circle(shape):
    def init(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
class Rectangle(shape):
    def init(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
circle=circle(5)
rectangle=Rectangle(4,6)
print("Area of the circle:",circle.area())
print("Area of rectangle:",rectangle.area())