"""HW02.py: Quick Baked Pi"""
__author__ = "James Garrett"
__credits__ = ["Joe Snider"]
__email__ = "garretjb@mail.uc.edu"
from math import sin,cos

#Fixed Point Approximation------------------------------------------------------
def approx_fixed_point(f, x):
    if (abs(f(x) - x) <= 1e-15):
        #print ("True") #Landmark - Check if works
        return True
    else:
        #print ("False") #Landmark - Check to see if code reached this
        #print (f(x), x) #Check to see if variables changed
        return False

def fixed_point_iteration(f, x=1.0):
    """
    >>> print(fixed_point_iteration(lambda x: sin(x) + x, 3.0))
    (3.141592653589793, 3)
    >>> print(fixed_point_iteration(lambda x: cos(x), 1.0))
    (0.7390851332151611, 86)
    """
    step = 0
    while not approx_fixed_point(f, x):
        x = f(x)
        step += 1
    return x, step

#Newton Find Zero---------------------------------------------------------------
step = 0

def find_zero(f, df, x):
    global step
    #print ("@find_zero") #Landmark - check if code reached this
    if (abs(f(x)) <= 1e-15):
        #print (x, step)
        x = x - f(x) / df(x)
        return x, step
    else:
        #print ("Ans is Wrong") #Landmark - check if code reached this
        x = x - f(x) / df(x) #Update it once
        step += 1 #Increment step count
        return (find_zero(f, df, x)) #Repeat Function

def newton_find_zero(f, df, x):
    """
    >>> print(newton_find_zero(lambda x: sin(x), lambda x: cos(x), 3.0))
    (3.141592653589793, 3)
    >>> print(newton_find_zero(lambda x: cos(x) - x , lambda x: -sin(x)-1, 1.0))
    (0.7390851332151607, 7)
    """
    #Code will first check to see if function f(x) is acceptably close to zero,
    #if it is within 10^-15, the code returns the value x and the step count.
    #if it is not, the code updates the value x, then reevaluates if the
    #function is acceptably close to zero. This repeats until the function f(x)
    #is within 10^-15 to zero, then outputs x and step count.
    return find_zero(f, df, x)

#Fixed point and Newton's method compute the number Pi at the same number of
#iterations, but Newton's method requires many less iterations than Fixed point
#to compute Dottie number to the acceptable accuracy.


#Run
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
