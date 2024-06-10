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

def scale_series(s, factor):
    return map(lambda x: x * factor, s)

def cos_series():
    yield 1
    yield from scale_series(integrate_series(sin_series()), -1)

def pi_summands():
    sign = -1
    for i in integers_from(1):
        sign *= -1
        yield sign / (2 * i - 1)

def pi_stream():
    yield from scale_series(partial_sums(pi_summands()), 4)

def euler_transform(s):
    s0 = next(s)
    s1 = next(s)
    s2 = next(s)
    while True:
        denominator = s0 - 2 * s1 + s2
        if denominator != 0:
            yield s2 - (s2 - s1) ** 2 / denominator
        else:
            # 可以选择在这里yield None或者某个特定的错误值，或者直接跳过
            pass
        s0, s1, s2 = s1, s2, next(s)

def make_tableaus(transform, s):
    yield s
    for t in make_tableaus(transform, transform(s)):
        yield t

def pi_tableaus():
    for t in make_tableaus(euler_transform, pi_stream()):
        yield next(t)

if __name__ == '__main__':
    for pi, i in zip(pi_stream(), integers_from(1)):
        print(pi)
        if i > 10:
            break

    for pi_transformed, i in zip(euler_transform(pi_stream()), integers_from(1)):
        print(pi_transformed)
        if i > 10:
            break

    pi_tableau_gen = pi_tableaus()
    for i in range(1, 11):
        print(next(pi_tableau_gen))