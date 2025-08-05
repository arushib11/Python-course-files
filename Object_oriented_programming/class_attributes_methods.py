# Circle class
class Circle:
    pi=3.14
    
    @classmethod
    def area(cls,radius):
        return cls.pi*(radius**2)
    
    @classmethod
    def perimeter(cls,radius):
        return cls.pi*2*radius
    
    @classmethod
    def get_area_perimeter(cls,radius):
        return cls.area(radius),cls.perimeter(radius)

print(Circle.area(4))
print(Circle.perimeter(4))
print(Circle.get_area_perimeter(4))

# Employee class
class Employee:
    average_age=0
    average_salary=0
    total_age=0
    total_salary=0
    count=0

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        Employee.count+=1
        Employee.total_age=Employee.total_age+self.age
        Employee.total_salary=Employee.total_salary+self.age
        Employee.average_age=(Employee.total_age)/Employee.count
        Employee.salary=(Employee.total_salary)/Employee.count

e1=Employee("George",34,65000)
print(Employee.average_age)
print(Employee.average_salary)
e2=Employee("Sarah",25,95000)
print(Employee.average_age)
print(Employee.average_salary)

# Temperature Class
class Temperature:
    min_temperature=0
    max_temperature=1000

    def __init__(self,kevin):
        if Temperature.min_temperature<=kevin<=Temperature.max_temperature:
            self.kevin=kevin
        else:
            raise Exception("Entered temperature must be between min and max inclusive.")
    
    @classmethod
    def update_min_temperature(cls,kevin):
        if kevin>cls.max_temperature:
            raise Exception("This temperature cannot exceed Max temperature.")
        else:
            cls.min_temperature=kevin

    @classmethod
    def update_max_temperature(cls,kevin):
        if kevin<cls.min_temperature:
            raise Exception("This temperature cannot be below Min temperature.")
        else:
            cls.max_temperature=kevin

t1=Temperature(260)
Temperature.update_max_temperature(270)
#Temperature.update_min_temperature(680)
#t2=Temperature(280)
Temperature.update_min_temperature(100)
t3=Temperature(120)
Temperature.update_max_temperature(90)


