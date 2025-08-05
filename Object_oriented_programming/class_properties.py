class Person:
    def __init__(self,name):
        self.name=name
        self._salary=0
    
    @property                    #new way
    def salary(self):
        return round(self._salary)

    @salary.setter
    def salary(self,salary):
        if salary<0:
            raise ValueError("This is invalid!")
        self._salary=salary

    
    
   # salary=property(get_salary,set_salary) legacy way

p=Person("Tim")
p.salary=100.998
print(p.salary)
