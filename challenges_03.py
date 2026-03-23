import math
import sys
import string

def ints_only(a, b):
    if isinstance(a,int) and isinstance(b,int):
        return True
    else:
        return False

boolean = ints_only('2',1)
print(boolean)