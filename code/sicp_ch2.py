def is_list(z):
    return isinstance(z, list)


def is_nested(li):
    return any(isinstance(i, list) for i in li)


def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]


def tree_map(map_fn, tree):
    return apply_to_all(lambda subtree: tree_map(map_fn, subtree) if is_list(subtree) else map_fn(subtree), tree)


def scale_tree(li, factor):
    scale = lambda x: x * factor
    return tree_map(scale, li)


def square_tree(li):
    square = lambda x: x * x
    return tree_map(square, li)


def subset(s):
    if not s:
        return [[]]
    else:
        rest = subset(s[1:])
        return rest + apply_to_all(lambda x: s[0:1] + x if is_list(x) else s[0:1] + [x], rest)
