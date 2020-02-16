"""HW01.py: Egyptian Greedy Algorithm"""
__author__ = "James Garrett"
__credits__ = ["Joe Snider"]
__email__ = "garretjb@mail.uc.edu"

s = ''
num = int(input("Please input a numerator: "))
den = int(input("please input a denominator: "))
#Formula

def calc(num, den):
    global s

    if den == 0 or num == 0:
        return

    if int (den%num) == 0:
        s += ("1/"+str(int(den/num)))
        return

    if (num%den) == 0:
        s += (int(num/den))
        return

    if num>den:
        s += (int(num/den),"+")
        calc (num%den,den)
        return

    n = int(den/num) + 1
    s += ("1/"+str(n)+ " + ")
    calc(int(num*n-den),int(den*n))
calc(num, den)
print(s, "=", str(num)+"/"+str(den))


def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
