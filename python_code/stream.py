def sieve(stream):
    prime = next(stream)
    yield prime
    yield from sieve(filter(lambda x: x % prime != 0, stream))

def integers_from(n):
    while True:
        yield n
        n += 1

def primes():
    yield from sieve(integers_from(2))

def ones():
    while True:
        yield 1

def add_streams(s1, s2):
    for i, j in zip(s1, s2):
        yield i + j

def other_integers():
    yield from add_streams(integers_from(0), ones())

def factorial():
    n = 1
    for i in integers_from(1):
        n *= i
        yield n

def partial_sums(stream):
    s = 0
    for i in stream:
        s += i
        yield s

def merge(s1, s2):
    i = next(s1)
    j = next(s2)
    while True:
        if i < j:
            yield i
            i = next(s1)
        elif i > j:
            yield j
            j = next(s2)
        else:
            yield i
            i = next(s1)
            j = next(s2)

def scale_stream(s, factor):
    return map(lambda x: x * factor, s)

def hamming_numbers():
    def numbers():
        yield 1
        for n in merge(scale_stream(numbers(), 2), merge(scale_stream(numbers(), 3), scale_stream(numbers(), 5))):
            yield n
    return numbers()

def integrate_series(s):
    i = 1
    for n in s:
        yield n * 1 / i
        i += 1

def exp_series():
    yield 1
    yield from integrate_series(exp_series())

def sin_series():
    yield 0
    yield from integrate_series(cos_series())

def cos_series():
    yield 1
    yield from scale_series(integrate_series(sin_series()), -1)

if __name__ == '__main__':
    # for p in primes():
    #     print(p)
    #     if p > 100:
    #         break

    # for i in other_integers():
    #     print(i)
    #     if i > 100:
    #         break

    # for i in partial_sums(integers_from(1)):
    #     print(i)
    #     if i > 10:
    #         break

    # for i in factorial():
    #     print(i)
    #     if i > 30:
    #         break

    # for i in hamming_numbers():
    #     print(i)
    #     if i > 100:
    #         break

    for i in exp_series():
        print(i)
        if i > 10:
            break

    # for i in sin_series():
    #     print(i)
    #     if i > 10:
    #         break

    # for i in cos_series():
    #     print(i)
    #     if i > 10:
    #         break
