class Page:
    def __init__(self,words,page_number):
        self.words=words
        self.page_number=page_number
    
    # overriding the addition method to add two pages
    def __add__(self,other):   # the self is the first object and 'other' is the second object
        new_words=self.words+" "+other.words
        new_page_number=max(self.page_number,other.page_number)+1
        return Page(new_words,new_page_number)

page1=Page("Tim is a great instructor!",1)
page2=Page("This is another page.",2)
# We want page1+page2->page3 and page number should be next number
page3=page1+page2 # trying out a random thing
print(page3.words,page3.page_number)

class StoreItem:
    TAX=0.13

    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.after_tax_price=0
        self.set_after_tax_price()

    def set_after_tax_price(self):
        self.after_tax_price=self.price*(1+self.TAX)

    # overriding substract dunder method so that we can substract int from the object
    def __sub__(self,discount):
        return StoreItem(self.name,self.price-discount)
    # overriding multiplication operator to reflect discounted 
    def __mul__(self,value):
        return StoreItem(self.name,self.price*value)
       
bread=StoreItem("Bread",7)
discounted=bread-2  # we want to be able to do that to substract the discount price directly from the item
print(round(discounted.after_tax_price,2))
discounted_bread=bread*0.5
print(round(discounted_bread.after_tax_price,2))

import math

class Line:
    def __init__(self,point1,point2):  #  (point1,pointy)
        self.point1=point1
        self.point2=point2
# trying to create a division such that individual points will be divided by factor
    def __truediv__(self,factor): #regular division floordiv for integer division
        new_point1=(self.point1[0]/factor,self.point1[1]/factor)
        new_point2=(self.point1[0]/factor,self.point2[1]/factor)
        return Line(new_point1,new_point2)
    def __floordiv__(self,factor): #regular division floordiv for integer division
        new_point1=(self.point1[0]//factor,self.point1[1]//factor)
        new_point2=(self.point1[0]//factor,self.point2[1]//factor)
        return Line(new_point1,new_point2)
    
# overriding len function to calculate the length of the line
    def __len__(self):   # from len we must return an ineteger
        distance_x=(self.point1[0]-self.point2[0])**2
        distance_y=(self.point1[1]-self.point2[1])**2
        dis=math.sqrt(distance_x+distance_y)
        return round(dis)
    
# overriding comparison operation == and != since lines with same coordinates return False
# since line 1 and line2 are different objects, storing different objects
    def __eq__(self,other):
        # checking for type equality first
        if not isinstance(other,Line):
            return False
        return self.point1==other.point1 and self.point2==other.point2
    
# overriding not equal to operator
    def __ne__(self,other):
        return not self.__eq__(other)

# overriding greater than to operator
    def __gt__(self,other):
        return len(self)>len(other)
    
# overriding greater than equal to to operator
    def __ge__(self,other):
        return len(self)>=len(other)
    
# overriding less than to operator
    def __lt__(self,other):
        return len(self)<len(other)
    
# overriding less than equal to to operator
    def __le__(self,other):
        return len(self)<=len(other)

line1=Line((20,5),(20,10))
line2=line1/2
print(line2.point1,line2.point2)

line3=line1//2
print(line3.point1,line3.point2)

line4=Line((10,5),(20,9))
print(len(line4))

line1=Line((20,5),(20,10))
line2=Line((10,5),(20,10))
print(line1!=line2)
print(line1==line2)

line1=Line((10,5),(20,9))
line2=Line((0,5),(20,9))
print(line1>line2)
print(line1>=line2)




