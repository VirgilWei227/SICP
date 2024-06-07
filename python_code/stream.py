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

if __name__ == '__main__':
    for p in primes():
        print(p)
        if p > 100:
            break

    for i in other_integers():
        print(i)
        if i > 100:
            break

    for i in partial_sums(integers_from(1)):
        print(i)
        if i > 10:
            break