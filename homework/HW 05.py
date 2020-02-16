__author__ = "Raymond Gee" # Your name
__credits__ = [""] # Your list of helpers
__email__ = "geern@mail.uc.edu" # Your email address
def sprout_leaves(t,vals):
    """Sprout new leaves containing the data in vals at each of
    the deepest leaf in the original tree t and return the resulting tree.
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
    
    if is_leaf(t):  #checks if the tree is a leaf
        leaves_add = [] #list to save the vals being inputed
        for i in vals:  #converts the vals into a tree
            leaves_add += [tree(i)]
        return tree(root(t),leaves_add) #returns the leaf and vals

    there_is_more = 0   #variable for if there is a branch that isn't a leaf
    
    for i in branches(t):   #goes to each branch
        if not is_leaf(i):  #checks if branch isn't a leaf
            there_is_more = 1   #changes the variable

    kept_branches = []  #list to hold branches that need to be added back

    if there_is_more == 1:  #checks if there is a branch that isn't a leaf
        for i in branches(t):   #goes through each branch
            if is_leaf(i):  #checks if the branch is a leaf
                kept_branches += [i]    #adds the branch to the list
            else:
                kept_branches += [sprout_leaves(i,vals)]    #if the branch isn't a leaf, calls back the function
    elif there_is_more == 0:    #checks if there is branches without leaves
        new_branches = []   #list to hold branches that need to be added back
        for i in branches(t):   #goes to each branch
            new_branches += [sprout_leaves(i,vals)] #calls back the function to add leaves
        return tree(root(t), new_branches)  #returns the root and new branches
    return tree(root(t), kept_branches) #returns the new tree

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
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

##predefining variables for testing purposes
##t1 = tree(1, [tree(2), tree(3, [tree(4)])])
##t2 = tree(1, [tree(2), tree(3, [tree(4, [tree(5), tree(6)])])])
##new1 = sprout_leaves(t1,[5,6])
##print_tree(new1)

def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    _test()
