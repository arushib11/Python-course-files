'''# Trying out basic Set functionalities
x=set()
y={1,2,3}
x.add(11)
x.add(12)
x.add(13)
print(x,"\n",y)
y.add(3)
print(y)
y.remove(1)
print(y)
y.clear()
print(x,"\n",y)
print(len(x))
print(1 in x)
print("********************************")

#Set operations
x={1,2,5}
y={3,4,5}
z=x.union(y)
print(z,x,y)
i=x.intersection(y)
print(i)
d1=x.difference(y)
d2=y.difference(x)
print(d1,d2)
sd=y.symmetric_difference(x)
print(sd)
x.update(y)
print(x,y)
x={1,2,5}
y={3,4,5}
x.difference_update(y)
print(x,y)
x={1,2,5}
y={3,4,5}
x.symmetric_difference_update(y)
print(x,y)
x={1,2,5}
y={1,2,3,4,5}
print(x.issubset(y))
print(y.issubset(x))

# Example of set
x=[1,2,3,2,2,3,1,3,4]
set_x=set(x)
print(set_x)

# Program that asks user to enter characters until user enters same character or more than one character
'''
x=set()
while True:
    c=input("Enter a character: ")
    if c in x:
        break
    if len(c)>1:
        break
    x.add(c)
print(f"Number of unique characters entered: {len(x)}")
