from Tree import *
from Linked_list import *

def empty(s):
    return s is Link.empty


def set_contains(s, v):
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)


def adjoin_set(s, v):
    """Return a set containing all elements of s and element v."""
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)


def intersect_set(set1, set2):
    """Return a set containing all elements common to set1 and set2."""
    return filter_link(lambda v: set_contains(set2, v), set1)


def union_set(set1, set2):
    """Return a set containing all elements either in set1 or set2."""
    set1_not_set2 = filter_link(lambda v: not set_contains(set2, v), set1)
    return extend_link(set1_not_set2, set2)
