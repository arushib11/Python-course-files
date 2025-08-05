# A function that accepts a dictionary "frequencies" and two strings "string1" & "string2".
# The dictionary contains character keys and integer values. The function should return 0,1 or 2 according to the cases below:
# returns 2 if frequency of char in dictionary is sufficient to create both string1 and string 2 without resuing any chars
# returns 1 if frequency of char in dictionary is sufficient to create either string1 or string 2 without resuing any chars
# returns 0 if frequency of char in dictionary is not sufficient to create either string1 or string 2 without resuing any chars

def create_string_from_characters(frequencies,string1,string2):

    s=list(set(string1))
    
    for elem in string1:
        if string1.count(elem)>frequencies[elem]:
            flag1=0
            break
        else:
            flag1=1

    for elem in string2:
        if string2.count(elem)>frequencies[elem]:
            flag2=0
            break
        else:
            flag2=1
    if flag1==0 and flag2==0:
        f_flag=0
    if flag1 and flag2:
        f_flag=2
    elif flag1 or flag2:
        f_flag=1

    return f_flag

frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"

f=create_string_from_characters(frequencies,string1,string2)
print(f)
'''
frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"
expected=1

frequencies = {"a": 3, "b": 5, "c": 3, "d": 2, "e": 1}
string1 = "aaabbbc"
string2 = "bbccde"
expected = 2

frequencies = {"a": 3, "b": 1, "c": 3, "d": 2, "e": 1}
string1 = "aaabbbc"
string2 = "bbccde"
expected = 0'''

