from operator import *

def arithmetic_operation(operation):
    kw = {"+" : add,
       "-" : sub,
       "*" : mul,
       "/" : truediv}
    return kw[operation]

