'''try:
    z=float("hi")
except ZeroDivisionError as e:
    print("zero exception",e)
except Exception as e:
    print("Other exception")
print("Done")

#raise Exception("This is an error!!")

# Practice raising our own exceptions

while True:
    n=input("Enter a number: ")

    try:
        n=float(n)
        break
    except ValueError as e:
        print("Not a float, try again!")'''

# Program asking a user for 2 numbers: numerator and denominator. Program should divide and handle exception.

num=input("Enter a numerator: ")
den=input("Enter a denominator: ")
try:
    int(num)
except Exception as e:
    print("The numerator is not a number.")

try:
    int(den)
except ValueError as e:
    print("The denominator is not a number.")
    
try:
    res=int(num)/int(den)
    print(f"The result of this division is {res}")
except ZeroDivisionError as e:
    print("You cannot divide by 0.")
    print("This division cannot be performed.")
except Exception as e:
        print("This division cannot be performed.")
finally:
    print("Goodbye!")
    