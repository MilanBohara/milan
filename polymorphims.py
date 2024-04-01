#calculating the area of different shapes . We'll crate a base class shape with an area() method, and than create subclassesfor specific shapes like Rectangle , Crircle, and Tringle which will override the area() method to calculate the specific to each shape.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, redius):
        self.redius = redius

    def area(self):
        return math.pi * self.redius ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
# Creating instances of different shapes
    
rectangle = Rectangle(5,4)
circle = Circle(3)
triangle = Triangle(6,8)

#Calcul;ating area without knowing specific types
print("Area of Rectanglke:" , circle.area())
print("Area of Circle:" , circle.area())
print("Area of Triangle:" , triangle.area())
