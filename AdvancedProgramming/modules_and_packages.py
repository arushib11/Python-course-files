## Absolute Imports ##
# Multiple ways of importing "a.py" within "code" package
# import code.a
# from code.a import A
# import code   #when "init" file of "code" imports "A()" for "code" to access it directly
# from code import A,B

## Relative imports ##
import code.a


# Multiple ways of accessing "A()"

#code.a.A()
#A()
#code.A()   # when "init" file of "code" imports "A()" for "code" to access it directly
