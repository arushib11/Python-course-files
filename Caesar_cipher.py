# Write a function that accepts a string and returns the caesar cipher encoding of that string according to a
# secondary input parameter name offset. Offeste will be a positive integer and string lowercase.

# abcdefghijklmnopqrstuvwxyz


def caesar_cipher(str,offset):
    s=[]

    for elem in str:
        ord_char=ord(elem)
        if ord_char-offset>=97:
            new_ord_char=ord_char-offset
        else:
            new_ord_char=123-offset+(ord_char-97)   
        new_char=chr(new_ord_char)
        s.append(new_char)
    return "".join(s)

s1=caesar_cipher("apple",5)
print(s1)

# more efficient solution

def caesar_cipher(str,offset):
   new_string=''
   alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

   for elem in str:
       position=alphabet.index(elem)
       new_position=position-offset
       new_char=alphabet[new_position]
       new_string+=new_char

   return new_string

s1=caesar_cipher("hello",3)
s2=caesar_cipher("apple",5)
print(s1,s2)

# Learnt the importance of index and lists




