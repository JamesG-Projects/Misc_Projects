"""Lab11.py: Coroutines"""
__author__ = "James Garrett"
__credits__ = [""]
__email__ = "garretjb@mail.uc.edu"

#####################
# Lab11 Co-Routines #
#####################

def supplier(ingredients, chef):
    for ingredient in ingredients:
        try:
            chef.send(ingredient)
        except StopIteration as e:
            print(e)
            raise
    chef.close()


def customer():
    served = False
    while True:
        try:
            dish = yield
            print('Yum! Customer got a {}!'.format(dish))
            served = True
        except GeneratorExit:
            if not served:
                print('Customer never got served.')
            raise

def chef(customers, dishes):
    """
    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun', 'hotdog'], c)
    Yum! Customer got a hotdog!
    Chef went home.

    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun'], c)
    Chef went home.
    Customer never got served.

    >>> cust = customer()
    >>> next(cust)
    >>> c = chef({cust: 'hotdog'}, {'hotdog': ['bun', 'hotdog']})
    >>> next(c)
    >>> supplier(['bun', 'hotdog', 'mustard'], c)
    Yum! Customer got a hotdog!
    No one left to serve!
    """
    remaining_customers = dict(customers)
    ingredients = set()
    while True:
        try:
            ingredient = yield
        except GeneratorExit:
            print('Chef went home.')
            for customer in customers:
                customer.close()
            raise

        ingredients.add(ingredient)

        if not remaining_customers:
            raise StopIteration('No one left to serve!')

        for customer, dish_name in dict(remaining_customers).items():
          if not set(dishes[dish_name]) - ingredients:
              customer.send(dish_name)
              del remaining_customers[customer]


#Run
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
