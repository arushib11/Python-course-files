#trying different dictionary functionalities

x={"a":1,"b":2,"c":3}
print(x["a"])
print(x.keys())
print(x.values())
x["d"]=4
print(x.keys())
print(x.values())
x["d"]=5
v=list(x.values())
print(v)
print(v[2])
del x["d"]
print(x.keys())
print(x.values())
c="a" in x
print(c)
i=list(x.items())
print(i)
print(f"length={len(x)}.")

for key in x:
    value=x[key]
    print(key,value)

for key,value in x.items():
    print(key,value)

x["c"]=x.get("c",0)+1
print(x)
x["c"]=x.get("c",0)+1
print(x)
print("**********************************************")

# Counting frequency of characters in a given string

characters={}
string="hello world"
for char in string:
    characters[char]=characters.get(char,0)+1
print(characters)

print("**********************************************")

# Counting frequency of numbers entered by a user util user enters 'q'

counts={}
while True:
    num=input("Number (enter q to quit): ")
    if num=="q":
        break
    num=int(num)
    counts[num]=counts.get(num,0)+1
print(counts)

# Counting frequency of characters in a string entered by a user

freq={}
usr_inp=input("Enter a string: ")
for char in usr_inp:
    freq[char]=freq.get(char,0)+1
for char in freq:    
    print(f"{char}: {freq[char]}")

