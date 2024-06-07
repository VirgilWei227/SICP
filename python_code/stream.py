def sieve(stream):
    prime = next(stream)
    yield prime
    yield from sieve(filter(lambda x: x % prime != 0, stream))

def integers():
    n = 2
    while True:
        yield n
        n += 1

def primes():
    yield from sieve(integers())

if __name__ == '__main__':
    for p in primes():
        print(p)
        if p > 100:
            break