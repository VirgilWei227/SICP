def integral(integrand, initial_value, dt):
    """
    Compute the integral of a function using a generator.
    """
    total = initial_value
    for i in integrand:
        total += i * dt
        yield total

def scale_stream(s, factor):
    return map(lambda x: x * factor, s)

def add_stream(s1, s2):
    for i, j in zip(s1, s2):
        yield i + j

def RC(R, C, dt):
    def proc(i, v0):
        yield from add_stream(scale_stream(i, R), integral(scale_stream(i, 1 / C), v0, dt))

    return proc


if __name__ == '__main__':
    RC1 = RC(5, 1, 0.5)
    it = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5] + [1.5] * 100
    for vt in RC1(it, 0):
        print(vt)