class Stream:
    """A lazily computed linked list."""

    class empty:

        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))


def integer_stream(first):
    def compute_rest():
        return integer_stream(first + 1)
    return Stream(first, compute_rest)

if __name__ == '__main__':
    s = integer_stream(1)
    print(s.first)
    print(s.rest.first)
    print(s.rest.rest.first)
    print(s.rest.rest.rest.first)
    print(s.rest.rest.rest.rest.first)
    print(s.rest.rest.rest.rest.rest.first)
    print(s.rest.rest.rest.rest.rest.rest.first)
    print(s.rest.rest.rest.rest.rest.rest.rest.first)
    print(s.rest.rest.rest.rest.rest.rest.rest.rest.first)
    print(s.rest.rest.rest.rest.rest.rest.rest.rest.rest.first)