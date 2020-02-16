"""HW01.py: Egyptian Greedy Algorithm"""
__author__ = "James Garrett"
__credits__ = ["Joe Snider"]
__email__ = "garretjb@mail.uc.edu"

#Variables
s = ''
n = int(input("Enter Numerator: "))
d = int(input("Enter Denominator: "))

#Function
def greedy(n, d):
    global s

    if d == 0 or n == 0:
        return

    if int(d % n) == 0:
        s += ("1/"+str(int(d/n)))
        return

    if (n % d) == 0:
        s += (int(n/d))
        return

    if n > d:
        s += (int(n/d)," + ")
        greedy(n % d, d)
        return

    x = int(d / n) + 1
    s += ("1/"+str(x)+" + ")
    greedy(int(n * x - d), int(d * x))
greedy(n, d)
print(s, "=", str(n)+"/"+str(d))

#Run
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
