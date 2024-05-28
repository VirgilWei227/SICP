def element_of_set(x, s):
    return x in s

def intersection_of_sets(s1, s2):
    return s1.intersection(s2)

def union_of_sets(s1, s2):
    return s1.union(s2)

def difference_of_sets(s1, s2):
    return s1.difference(s2)

if __name__ == "__main__":
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}
    print(element_of_set(1, s1))
    print(intersection_of_sets(s1, s2))
    print(union_of_sets(s1, s2))
    print(difference_of_sets(s1, s2))
    