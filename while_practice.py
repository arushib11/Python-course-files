# A program that uses while loop to continually ask the user to enter a number until they enter
# number 5, at which point, the program prints how many numbers the user has entered.
count=0
while True:
    count+=1
    num=int(input("Enter a number: "))
    if num==5:
        print(f"You entered {count} numbers.")
        break

print("**********************************************")

# A program that uses while loop to continually ask the user to enter a word until they enter
# 'q' or 'quit' , at which point, the program prints average length of words the user has entered.
#excluding the 'q' or 'quit'. If user doesnt enter any words, your program shouldn't print anything.

count=0
l=0

while True:
    w=input("Enter a word: ")

    if w !='q' and w!='quit':
        count+=1
        l+=len(w)
        avg=l/count
    if w=='q'or w=='quit':
        break

if l!=0:
    print(f"The average word length is: {avg}.")

print("**********************************************")

# Use a while loop to print squares of the numbers 1,3,6,10,15,21
count=0
num=0
while count<6:
    count+=1
    num=num+count
    print(num*num)
