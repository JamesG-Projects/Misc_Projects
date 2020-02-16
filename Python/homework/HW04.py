"""HW04.py: Reducing Linked Lists"""
__author__ = "James Garrett"
__credits__ = [""]
__email__ = "garretjb@mail.uc.edu"

def reduce_links(lst):
    """
    >>> lst = link(5, link(3, link(-2, link(-1, link(-5, link(2))))))
    >>> reduce_links(lst)
    [2, 'empty']
    >>> lst = link(2, link(-2, link(-1, link(-5, link(2)))))
    >>> reduce_links(lst)
    [-1, [-5, [2, 'empty']]]
    """
    value = lst[0]
    i = 1
    def recursion(lst,value,i):
        while (len(lst) != 1) and (value != 0):
            #print("Value: ", value) #Debugging
            if (i == 0):
                value += lst[i]
                i = 1
                #print("Value: ", value) #Debugging
            else:
                i = 0
                return recursion(lst[1], value, i)
        return lst[1]
    return recursion(lst,value,i)

#===========================================================================
#The code in this chunk is my different attempts at solving the problem
#print("third one: ", lst[1][1][0])
"""
i = 0
while len(lst) is 2:
    if (lst[0] + lst[1][0] is 0):
        lst

cont = True
while cont is True:
    i = 0
    j = 1
    while len(lst) > 1:
        if (lst[i] + lst[j]) == 0:
"""
#===========================================================================

# Linked list ADT

# Linked List definition
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

#Run
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
