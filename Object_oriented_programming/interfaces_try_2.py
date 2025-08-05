import math


class ShapeInterface:
    def get_area(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError()


# Write your code here.
class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length
    def get_area(self):
        return self.side_length*self.side_length
        
    def get_perimeter(self):
        return 4*self.side_length       
    


class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return math.pi*(self.radius**2)
    def get_perimeter(self):
        return math.pi*2*self.radius
