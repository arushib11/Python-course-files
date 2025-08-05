import math

class Polygon:
    def get_area(self):
        raise NotImplementedError("Need to implement get_area")
    def get_sides(self):
        raise NotImplementedError("Need to implement get_area")
    def get_perimeter(self):
        return sum(self.get_sides())
    
class Triangle(Polygon):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def get_area(self):
        s=(self.side1+self.side2+self.side3)/2
        A=math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-s.side3))
        return A
    def get_sides(self):
        return [self.side1,self.side2,self.side3]

class Rectangle(Polygon):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def get_sides(self):
        return [self.width,self.height,self.width,self.height]
    
    def get_area(self):
        return self.width*self.height    
    
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
import math

class Polygon:
    def get_area(self):
        raise NotImplementedError("Need to implement get_area")
    def get_sides(self):
        raise NotImplementedError("Need to implement get_area")
    def get_perimeter(self):
        return sum(self.get_sides())
    
class Triangle(Polygon):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        #self.sides=[side1,side2,side3] this can be done too
    def get_area(self):
        #side1,side2,side3=self.sides  unpacking
        s=(self.side1+self.side2+self.side3)/2
        A=math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
        return A
    def get_sides(self):
        return [self.side1,self.side2,self.side3]
        #return seld.sides

class Rectangle(Polygon):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def get_sides(self):
        return [self.width,self.height,self.width,self.height]
    
    def get_area(self):
        return self.width*self.height    
    
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)


'''
** Checks done **
    def test_case_1(self):
        with self.assertRaises(NotImplementedError):
            Polygon().get_sides()
        with self.assertRaises(NotImplementedError):
            Polygon().get_area()
        with self.assertRaises(NotImplementedError):
            Polygon().get_perimeter()

    def test_case_2(self):
        triangle = Triangle(1, 1, 1)
        self.assertEqual(3, triangle.get_perimeter())
        rect = Rectangle(2, 3)
        self.assertEqual(10, rect.get_perimeter())
        square = Square(3)
        self.assertEqual(12, square.get_perimeter())

    def test_case_3(self):
        triangle = Triangle(1, 5, 6)
        self.assertEqual([1, 5, 6], sorted(triangle.get_sides()))
        rect = Rectangle(2, 3)
        self.assertEqual([2, 2, 3, 3], sorted(rect.get_sides()))
        square = Square(3)
        self.assertEqual([3, 3, 3, 3], sorted(square.get_sides()))

    def test_case_4(self):
        triangle = Triangle(2, 5, 6)
        self.assertAlmostEqual(4.68, triangle.get_area(), delta=0.01)
        rect = Rectangle(2, 3)
        self.assertEqual(6, rect.get_area())
        square = Square(5)
        self.assertEqual(25, square.get_area())

'''
