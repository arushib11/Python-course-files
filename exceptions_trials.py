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
except:
    print("The numerator is not a number.")
    print("This division cannot be performed.")
finally:
    print("Goodbye!")