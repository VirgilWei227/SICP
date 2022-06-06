from email.errors import InvalidMultipartContentTransferEncodingDefect


def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.
    >>> dice = make_test_dice(1, 2, 3)

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1

    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice


def f(x, y):
    return (lambda a, b: x * pow(a, 2) + y * b + a * b)(1 + x * y, 1 - y)


def fact_iter(product, counter, max_count):
    if counter > max_count:
        return product
    else:
        return fact_iter(product*counter, counter+1, max_count)


def fact(n):
    return fact_iter(1, 1, n)


def split(n):
    return n // 10, n % 10


def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_least, last = split(n)
        return sum_digits(all_but_least) + last


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def crust():
    print("70km")
    def mantle():
        print("2900km")
        def core():
            print("5300km")
            return mantle()
        return core
    return mantle


# def cons(x, y):
#     def dispatch(m):
#         if m == 0:
#             return x
#         else:
#             return y
#     return dispatch


def car(z):
    return z[0:1]


def cdr(z):
    return z[1:]


def cons(a, b):
    return a + b


def reverse(li):
    return li[::-1]


def is_list(z):
    return isinstance(z, list)


def is_nested(li):
    return any(isinstance(i, list) for i in li)


def deep_reverse(li):
    if not is_list(li):
        return li
    elif not li:
        return []
    elif not is_nested(li):
        return li[::-1]
    else:
        tmp = li[::-1]
        return [deep_reverse(x) for x in tmp]


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

