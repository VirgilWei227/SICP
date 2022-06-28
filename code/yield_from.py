def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
    else:
        yield 'Balst off'


def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s


def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])


# yield + return
def g(x):
    yield x
    yield x + 1
    return x + 2
    yield x + 3


def h(x):
    y = yield from g(x)
    print(y)
    yield y
