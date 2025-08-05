## setting up for absolute imports
# print("a")
# import code.b

## setting up for relative imports
from . import b      # . denotes current package 

def A():
    print("A")

b.B()