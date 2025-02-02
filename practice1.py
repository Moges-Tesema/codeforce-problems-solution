import numpy as np
import sys
# sys.setrecursionlimit(10)

def TwoPowerOf(n):
   
    if n<1:
        return 1
    else:
        power = TwoPowerOf(n-1)
        return power*2
# x=TwoPowerOf(4)
# print(f"output is {x:.2f}".format(x))
def factorail(n):
    assert n >= 0 and int(n) == n, "the number must be positive integer"
    if n in [0,1]:
        return 1
    else:
        return n * factorail(n-1)
fact4=factorail(5)
print("what is the answer?",fact4)