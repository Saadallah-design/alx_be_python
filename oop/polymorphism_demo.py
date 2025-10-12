# Objective: Enhance your understanding of polymorphism in Python 
# by creating a set of classes that 
# demonstrate method overriding and polymorphic behavior.



class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)