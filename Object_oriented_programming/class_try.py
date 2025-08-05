'''class Person:
    def __init__(self,x):
        print(f"Hi {x}.")

p1=Person(2)'''

'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("Bill",21)
p2=Person("Tim",44)

print(p1.name,p1.age)
print(p2.name,p2.age)

p1.new="random" #creating new attribute from outside class
print(p1.new)
p1.name="Arr"  #modifying attribute value from outside class
print(p1.name,p1.age)'''

# Create fruit class with name,calories

class Fruit:
    def __init__(self,name,calories):
        self.name=name
        self.calories=calories
f1=Fruit("Apple",100)
f2=Fruit("Banana",200)
print(f1.name,f1.calories)
print(f2.name,f2.calories)
f1.color="red"
