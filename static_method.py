'''class Student:
    grade_bump=2.0

    def __init__(self,name,grades=[]):
        self.name=name
        self.grades=grades
    
    def average(self):
        return sum(self.grades)/len(self.grades)

    @classmethod
    def average_from_grades_plus_bump(cls,grades):
        average=cls.Average(grades)
        return min(average+cls.grade_bump,100)  # interesting use of min function

    @staticmethod
    def Average(grades):
        return sum(grades)/len(grades)

s1=Student("Tim",[80,75,66,100])
s2=Student("Clement",[60,50,66,60])

average=s1.Average(s1.grades)
average2=s2.Average(s2.grades)

print(average)
print(average2)
'''

class Physics:

    @staticmethod
    def calculate_net_force(mass,acceleration):
        if mass<0 or acceleration<0:
            return 0.0
        return mass*acceleration
    
    @staticmethod
    def calculate_acceleration(mass,net_force):
        if mass<0 or net_force<0:
            return 0.0
        return net_force/mass
    
    @staticmethod
    def calculate_mass(net_force,acceleration):
        if net_force<0 or acceleration<0:
            return 0.0
        return net_force/acceleration