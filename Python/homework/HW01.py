"""HW01.py: Egyptian Greedy Algorithm"""
__author__ = "James Garrett"
__credits__ = ["Joe Snider"]
__email__ = "garretjb@mail.uc.edu"

import math
from fractions import Fraction

#Function
def greedy(num):

    result = []
    while num.numerator != 1:
        if num.numerator == 1: #if numerator is 1, code is done
            result.append(num)
            return result
        else:
            x = int(math.ceil(float(num.denominator/num.numerator)))
            #float causes the ints to not round down to zero, ceil rounds up to smallest int value
            frac = Fraction(1,x)
            result.append(frac)
            num = num - frac
            if num.numerator == 1:
                result.append(num) #if numerator is 1, the code is done
            # print("NUM: ", num) -> check that the above code was working

    #Print out resulting fractions
    print("-----------------------------------------------------------------------")
    print("RESULT: ")
    print(*result, sep = " + ")
    print("-----------------------------------------------------------------------")

#Get Variables
print("-----------------------------------------------------------------------")
n = int(input("Enter numerator: "))
d = int(input("Enter denominator: "))
num = Fraction(n,d)
print("Number Given: ", num)
greedy(num)

#Run
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
