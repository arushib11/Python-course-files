'''# Initailizing a list with numbers from 1 to 10

lst=[i for i in range(1,11)]
print(lst)

# Practicing list comprehensions

lst=[i/2 for i in range(1,11)]
print(lst)

# More practing for list comprehension

lst=[i/2 for i in range(1,11) if i%2==0]
print(lst)
'''
# Practicing list comprehension for nested for loops

lst=[i+j for i in range(1,11) for j in range(5)]
print(lst)

'''# Practicing set comprehension 

lst={i+j for i in range(1,11) for j in range(5)}
print(lst)
'''
# practicing dictionary comprehension

lst={j:i for i in range(1,11) for j in range(5)}
print(lst)

x,y=[1,2]
print(x,y)