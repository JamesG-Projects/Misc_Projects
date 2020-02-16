"""HW02.py: Quick Baked Pi"""
__author__ = ""
__credits__ = [""]
__email__ = ""
from math import sin,cos

#Fixed Point
def approx_fixed_point(f,x):
    n=10**-15
    if (abs(f(x)-x)>n):
        return False

    else:
        return True

def fixed_point_iteration(f, x=1.0):
    """
    >>> print(fixed_point_iteration(lambda x: sin(x) + x, 3.0))
    (3.141592653589793, 3)
    >>> print(fixed_point_iteration(lambda x: cos(x), 1.0))
    (0.7390851332151611, 86)
    """
    step=0
    while not approx_fixed_point(f,x):
        x=f(x)
        step+=1
    return x, step

#Newton's
step=0
def newton_find_zero(f,df,x):
    """
    >>> print(newton_find_zero(lambda x: sin(x), lambda x: cos(x), 3.0))
    (3.141592653589793, 3)
    >>> print(newton_find_zero(lambda x: cos(x) - x , lambda x: -sin(x)-1, 1.0))
    (0.7390851332151607, 7)
    """
    return zero(f,df,x)

#Helper Functions
def zero(f,df,x):
    if (approx_eq(f(x))==1):
        return x, step

    else:
        return (update(f,df,x))

def update(f,df,x):
    global step
    step+=1
    x=updateTwo(f,df,x)
    return zero(f,df,x)

def updateTwo(f,df,x):
    x=x-f(x)/df(x)
    return x

def approx_eq(f):
    i=10**-15
    if (abs(f)<(i)):
        return True

    else:
        return False


#Test Code
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
