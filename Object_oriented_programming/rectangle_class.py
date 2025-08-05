# Rectangle class with method change_position() that accepts x and y positions,get_position() and get_area() method

class Rectangle:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    
    def change_position(self,x,y):
        self.x=x
        self.y=y

    def get_position(self):
        return (self.x,self.y)
    
    def get_area(self):
        return self.width*self.height

rect=Rectangle(7, -9, 5, 5)
pos=rect.get_position()
print(pos)

