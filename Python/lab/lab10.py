"""Lab10.py: Iterators and Generators"""
__author__ = "James Garrett"
__credits__ = [""]
__email__ = "garretjb@mail.uc.edu"


#############
# Iterators #
#############
# Q1
class IteratorA: #Works Without Problem
    def __init__(self):
        self.start = 10

    def __next__(self):
        if self.start > 100:
            raise StopIteration
        self.start += 20
        return self.start

    def __iter__(self):
        return self

class IteratorB: #Does not work
    def __init__(self):
        self.start = 5

    def __iter__(self):
        return self

class IteratorC: #Does not work
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 10:
            raise StopIteration
        self.start += 1
        return self.start

class IteratorD: #Works, but is infinite
    def __init__(self):
        self.start = 1

    def __next__(self):
        self.start += 1
        return self.start

    def __iter__(self):
        return self

# Q2
class OddNaturalsIterator:
    """
    >>> odds = OddNaturalsIterator()
    >>> odd_iter1 = iter(odds)
    >>> odd_iter2 = iter(odds)
    >>> next(odd_iter1)
    1

    >>> next(odd_iter1)
    3

    >>> next(odd_iter1)
    5

    >>> next(odd_iter2)
    7

    >>> next(odd_iter1)
    9

    >>> next(odd_iter2)
    11
    """

    def __init__(self):
        self.current = 1

    def __next__(self):
        result = self.current
        self.current += 2
        return result

    def __iter__(self):
        return self

class EvenNaturalsIterator:
    """
    >>> evens = EvenNaturalsIterator()
    >>> even_iter1 = iter(evens)
    >>> even_iter2 = iter(evens)
    >>> next(even_iter1)
    0

    >>> next(even_iter1)
    2

    >>> next(even_iter1)
    4

    >>> next(even_iter2)
    0

    >>> next(even_iter2)
    2
    """

    def __init__(self):
        self.current = 0

    def __next__(self):
        result = self.current
        self.current += 2
        return result

    def __iter__(self):
        return EvenNaturalsIterator()

class DoubleIterator:
    """
    >>> doubleI = DoubleIterator()
    >>> dIter = iter(doubleI)
    >>> next(doubleI)
    2

    >>> next(doubleI)
    4

    >>> next(dIter)
    2

    >>> next(dIter)
    4

    >>> next(doubleI)
    8
    """
    def __init__(self):
        self.current = 2

    def __next__(self):
        result = self.current
        self.current += result
        return result

    def __iter__(self):
        return DoubleIterator()

class ThreeIterator:
    """
    >>> threeI = ThreeIterator()
    >>> tIter = iter(threeI)
    >>> next(threeI)
    10

    >>> next(threeI)
    7

    >>> next(tIter)
    4

    >>> next(tIter)
    1

    >>> next(threeI)
    -2
    """
    def __init__(self):
        self.current = 10
    def __next__(self):
        result = self.current
        self.current -= 3
        return result
    def __iter__(self):
        return self

# Q3
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:
    ...     print(char)
    """

    def __init__(self, str):
        self.str = str
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.str):
            raise StopIteration
        return self.str[self.i]

##############
# Generators #
##############

# Q4
def generator():
    """
    >>> g = generator()
    <generator object>

    >>> g == iter(g)
    True

    >>> next(g)
    Starting here
    Before yield
    0

    >>> next(g)
    After yield
    Before yield
    1

    >>> next(g)
    After yield
    Before yield
    2
    """
    print("Starting here")
    i = 0
    while i < 6:
        print("Before yield")
        yield i
        print("After yield")
        i += 1

def generator():
    """
    >>> h = generator()
    >>> iter(h) == h
    True

    >>> next(h)
    Starting
    foo 2
    2

    >>> next(h)
    bar
    6

    >>> next(h)
    foo 5
    5
    """
    print("Starting")
    i = 2
    while i < 6:
        print("foo", i)
        yield i
        i += 1
        print("bar")
        yield i*2
        i += 2

# Q5
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    for elem in s:
        yield elem * k

# Q6
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    while n >= 0:
        yield n
        n = n - 1

class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    def __init__(self, cur):
        self.cur = cur

    def __next__(self):
        if self.cur < 0:
            raise StopIteration
        self.cur -= 1
        return self.cur + 1


    def __iter__(self):
        """So that we can use this iterator as an iterable."""
        return self

# Q7
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    i = n
    while i > 1:
        yield i
        if i % 2 == 0:
            i //= 2
        else:
            i = i * 3 + 1
    yield i

# the naturals generator is used for testing scale and merge functions
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

#Run
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
