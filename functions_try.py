# Program that replaces every occurance of character in string2 from string1

def remove_chars(s1,s2):
    for ch in s2:
        s3=s1.replace(ch,"")
    return s3
s=remove_chars("hello world","lo")
print(s)

# Program that adds two lists

def add_list(any_list):
    sum=0
    for elem in any_list:
        sum+=elem
    return sum

def two_lists(l1,l2):
    sum1=add_list(l1)
    sum2=add_list(l2)
    return sum1,sum2

a,b=two_lists([1,2,3,4],[5,6,7])
print(a,b)

# Program that takes in a list of integers and return new list containing all odd numbers in order which they appear.

def find_all_odds(lst):
    new_lst=[]
    for elem in lst:
        if elem%2!=0:
            new_lst.append(elem)
    return new_lst

l=find_all_odds([1,2,3,4,5,6,5,5,3,2])
print(l)

# Write a function which takes list of strings and returns a new list containing lengths of strings in order

def string_lengths(strings):
    new_list=[]
    for s in strings:
        new_list.append(len(s))
    return new_list

s=string_lengths(["hello","this","is","a","beard","orange","blue"])
print(s)

# Write a function that aacepts two optional parameters, list1, list2. It should return number of unique elements
# between two lists. If list is not passed as a parameter, it should be treated as empty list.

def compare_lists(lst1=[],lst2=[]):
    l1=set(lst1)
    l2=set(lst2)
    n_l=l1&l2

    return n_l,len(n_l)

l=compare_lists(lst2=[1,2,3])
print(l)

# Write a function which takes a list and element to trim.It returns new list where the last elements_to_trim elements have been removed

def trim_list(lst,elements_to_trim):
    new_lst=lst
    while elements_to_trim:
        new_lst.pop()
        elements_to_trim-=1
    return new_lst
list=trim_list([1,3,34,"hi","yes",True,2.3],3)
print(list)

# Write a function which takes in a list of integers and returns new list of same legth where element at index i in new list is equal to numbers[0]+numbers[1]+...+numbers[i-1]+numbers[i]

def running_sums(numbers):

    new_lst=[]
    new_elem=0
    for i in range(len(numbers)):
        new_elem=new_elem+numbers[i]
        new_lst.append(new_elem)
    return new_lst

sums=running_sums([5,4,2,1,5,6,4])
print(sums)

    
