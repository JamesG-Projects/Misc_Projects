"""HW05.py: Sprout Leaves"""
__author__ = "James Garrett"
__credits__ = [""]
__email__ = "garretjb@mail.uc.edu"

def sprout_leaves(t,vals):
    """
    >>> t1 = tree(1, [tree(2), tree(3, [tree(4)])])
    >>> print_tree(t1)
    1
      2
      3
        4
    >>> new1 = sprout_leaves(t1, [5, 6])
    >>> print_tree(new1)
    1
      2
      3
        4
          5
          6
    >>> new2 = sprout_leaves(new1, [1, 2])
    >>> print_tree(new2)
    1
      2
      3
        4
          5
            1
            2
          6
            1
            2
    """


    """
    if is_leaf(t):
        return (tree(root(t), [tree(v) for v in vals]))

    remaining_branches = []
    for b in branches(t):
        #if is_leaf(b):
        remaining_branches += [sprout_leaves(b, vals)]

    return tree(root(t), remaining_branches)
    """

    """
    if is_leaf(t):
        return (tree(root(t), [tree(v) for v in vals]))

    return (tree(root(t), [sprout_leaves(b, vals) for b in branches(t)]))
    """
    """
    def dfs(t, depth):

        for b in branches(t):
            depth += 1
            print("depth: ", depth)
        for b in branches(t):
            if is_leaf(t):
                depth += 1
            print("depth: ", depth)
        return (tree(branches(t), depth))
    """
    """
    depth = 1
    print("depth: ", depth)
    for elem in t:
        depth = depth + 1
        print("depth: ", depth)

    if is_leaf():
        return (tree(root(t), [branches(depth) + vals]))

    #return (tree(root(t), [sprout_leaves(b,vals) for b in branches(t)]))
    """

    if is_leaf(t):
        add_these = [] #Holds the values to be added
        for v in vals: #Puts them into a tree
            add_these += [tree(v)]
        return tree(root(t), add_these)

    branch_and_leaf = 0 #If a branch has a leaf as well as another branch
    for b in branches(t):
        if not is_leaf(b):
            branch_and_leaf = 1 #Changes the variable if there is another branch

    remaining_branches = [] #Holds branches which will need adding back
    if branch_and_leaf == 1:
        for b in branches(t):
            if is_leaf(b):
                remaining_branches += [b]
            else:
                remaining_branches += [sprout_leaves(b, vals)]

    elif branch_and_leaf == 0: #If there isn't another branch
        add_branches = [] #Holds branches that will need adding back
        for b in branches(t):
            add_branches += [sprout_leaves(b, vals)] #Adds the leaves from vals
        return tree(root(t), add_branches) #Adds the branches back
    return tree(root(t), remaining_branches) #New vals have been added


# Tree ADT
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(root(t), [copy_tree(b) for b in branches(t)])


def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    kept_branches = []
    for b in branches(t):
        if (root(b) != target):
            kept_branches += [delete(b, target)]
    return tree(root(t), kept_branches)


#Run
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    _test()
