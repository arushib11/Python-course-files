'''num=9
if num>5:
	print("Greater than 5")
elif num<5:
	print("less than 5")
else:
	print("Zero")
print("Done")'''

num=float(input("Enter a number: "))

if num>0 and num%2==0:
    print("Even number !")

    num2=float(input("Enter another number: "))
    if num2<0:
        print("Negative number")
    else:
        print("Positive number")

    x=5

    result="ok" if x>5 else "not ok"
    print(result)