#List methods and functions
#len(),l.append(),l.pop(),l.remove(),lst.index(),lst.count(),lst.extend,in,lst1+lst2
lst=[1,2,3,True,"Hi","a",1.1,None]
print(lst)
print(len(lst))
lst.append(1)
print(lst)
lst.pop()
print(lst)
print(lst.count(1))
print(lst.index(1))
lst.remove(1.1)
print(lst)
print(1.1 in lst)
print("Hi" in lst)
lst2=[10,11,12]
lst3=lst+lst2
print(lst3)
print(lst)
lst.extend(lst2)
print(lst)

