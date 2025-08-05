class Person:               # parent/super/base class
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def say_hello(self):
        print("*****************")
        print(f"Hello, {self.first_name} {self.last_name}")
        print("*****************")

class Employee(Person):    # child/derived/sub class
    def __init__(self,first_name,last_name,salary): # overriding the constructor
        super().__init__(first_name,last_name)
        self.salary=salary
        
    def say_hello(self):     # overriding a method
        print("---------------")
        super().say_hello()
        print(f"My salary is {self.salary}")
        print("---------------")

    def test(self):
        print("test")

class Manager(Employee):
    def __init__(self,first_name,last_name,salary,department): # overriding the constructor
        super().__init__(first_name,last_name,salary)
        self.department=department

class Owner(Person):
    def __init__(self,first_name,last_name,net_worth): # overriding the constructor
        super().__init__(first_name,last_name)
        self.net_worth=net_worth

m=Manager("Tim","Huxta",75000,"Sports")
print(isinstance(m,Person))
#print(isinstance(o,Person))
#m=Manager("Tim","Huxta",50000,"Sports")
#m.say_hello()
#e=Employee("Tim","Hola",5000)
#e.say_hello()


